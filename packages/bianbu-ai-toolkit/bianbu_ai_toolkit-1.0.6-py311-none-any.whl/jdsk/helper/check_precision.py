#!/bin/bash
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Copyright (c) 2023, spacemit.com, Inc. All Rights Reserved
#
# =============================================================
#
# Author: hongjie.qin@spacemit.com
# Brief:  Commandline tool to check onnx model output data consistency with onnx runtime
# History:
# 2023/09/17  v0.0.1  init commit

# shell code:
#"""eval" set -xe """#"

# python code:
magic='--calling-python-from-/bin/bash--'
"""exec" $([[ $* =~ --gdb ]] && echo "gdb --args") python3 "$0" "$@" """#$magic"

# pylint: disable=unused-argument,unused-import,ungrouped-imports,wrong-import-position

import os
import argparse
from abc import ABC, abstractmethod
import onnx
from onnx import onnx_pb
import onnxruntime as rt
import numpy as np

__version__ = "0.0.1"

_HELP_TEXT = """
Usage Examples:

# check desired output with actual output directly(both npz and txt format are available)
python3 {fname} --desired desired.npz --actual actual.txt
# check desired output and actual output with given tolerance
python3 {fname} --desired desired.npz --actual actual.npz --atol 1e-5 --rtol 0
# check desired output with onnx model and input data
python3 {fname} --desired desired.txt --model model.onnx --input data.npz
""".format(fname=os.path.basename(__file__))

sep = "\n"
npz_with_pickle = False

#
#  onnx dtype names
#
# from tf2onnx.utils import ONNX_DTYPE_NAMES
ONNX_DTYPE_NAMES = {
    onnx_pb.TensorProto.FLOAT: "float32",
    onnx_pb.TensorProto.FLOAT16: "float16",
    onnx_pb.TensorProto.DOUBLE: "double",
    onnx_pb.TensorProto.INT32: "int32",
    onnx_pb.TensorProto.INT16: "int16",
    onnx_pb.TensorProto.INT8: "int8",
    onnx_pb.TensorProto.UINT8: "uint8",
    onnx_pb.TensorProto.UINT16: "uint16",
    onnx_pb.TensorProto.INT64: "int64",
    onnx_pb.TensorProto.STRING: "string",
    onnx_pb.TensorProto.BOOL: "bool",
    onnx_pb.TensorProto.COMPLEX64: "complex64",
    onnx_pb.TensorProto.COMPLEX128: "complex128",
}

# predefined onnxruntime ep
constant_to_provider_map = {
    'cpu': 'CPUExecutionProvider'
}
"""
constant_to_provider_map_all = {
    'tensorrt': 'TensorrtExecutionProvider',
    'cuda': 'CUDAExecutionProvider',
    'migraphx': 'MIGraphXExecutionProvider',
    'rocm': 'ROCMExecutionProvider',
    'openvino': 'OpenVINOExecutionProvider',
    'dnnl': 'DnnlExecutionProvider',
    'tvm': 'TvmExecutionProvider',
    'vitisai': 'VitisAIExecutionProvider',
    'qnn': 'QNNExecutionProvider',
    'nnapi': 'NnapiExecutionProvider',
    'js': 'JsExecutionProvider',
    'coreml': 'CoreMLExecutionProvider',
    'armnn': 'ArmNNExecutionProvider',
    'acl': 'ACLExecutionProvider',
    'dml': 'DmlExecutionProvider',
    'rknpu': 'RknpuExecutionProvider',
    'xnnpack': 'XnnpackExecutionProvider',
    'cann': 'CANNExecutionProvider',
    'azure': 'AzureExecutionProvider',
    'cpu': 'CPUExecutionProvider'
}
"""
try:
    import spacemit_ort
    constant_to_provider_map['jdsk'] = 'SpaceMITExecutionProvider'
except:
    pass
meta_bkds = list(constant_to_provider_map.keys())


def get_argsparser_precision(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to check onnx model precision with onnx runtime.",
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    # Args for quick checking precision
    parser.add_argument("--desired", type=str, required=True, help="expected output data file path(txt/npz). For txt file, always suppose the dtype is float.")
    # Case1: with actual output
    parser.add_argument("--actual", type=str, default=None, help="actual output data file path(txt/npz). For txt file, always suppose the dtype is float.")
    # Case2: with input data and onnx model
    parser.add_argument("--model", type=str, default=None, help="input model file path(onnx)")
    parser.add_argument("--input", type=str, default=None, help="input test data file path(txt/npz)")
    parser.add_argument("--target", type=str.lower, nargs='+', default=['cpu'], choices=meta_bkds, help="target platform(s), aka provider(s)")
    parser.add_argument("--intra_threads", type=int, default=0, help="intra_op_num_threads of onnxruntime session options")
    parser.add_argument("--inter_threads", type=int, default=0, help="inter_op_num_threads of onnxruntime session options")
    # Args for debugging
    parser.add_argument("--verbose", "-v", default=0, help="additive option, "
                                                           "-v: show verbose info, "
                                                           "-vv: print outputs", action="count")
    # Args for checking consistency between two models
    parser.add_argument("--diff_max", default=False, help="check maximum abs difference or not", action='store_true')
    parser.add_argument("--atol", type=float, default=1e-4, help="absolute tolerance(default: 1e-4)")
    parser.add_argument("--rtol", type=float, default=0, help="relative tolerance(default: 0)")
    return parser


def _clean_initializers(model, verbose = False):
    inits = [e.name for e in model.graph.initializer]
    index = len(model.graph.input)
    for obj in model.graph.input[::-1]:
        index -= 1
        if obj.name in inits:
            _ = model.graph.input.pop(index)
            if verbose:
                print("Remove initializer {} from graph input".format(obj.name))


def _get_type_proto_info(type_proto):
    if type_proto.HasField("tensor_type"):
        return ONNX_DTYPE_NAMES[type_proto.tensor_type.elem_type], [d.dim_value for d in type_proto.tensor_type.shape.dim]
    elif type_proto.HasField("sequence_type"):
        inner_type_proto = type_proto.sequence_type.elem_type
        elem_type, shape = _get_type_proto_info(inner_type_proto)
        return [elem_type], [shape]
    raise NotImplementedError(
            "get type proto info from {} not implemented".format(type_proto)
    )


def _get_input_value_info(model):
    type_info = [(_get_type_proto_info(vi.type)) for vi in model.graph.input]
    return [vi.name for vi in model.graph.input], [e[0] for e in type_info], [e[1] for e in type_info]


def _get_output_value_info(model):
    type_info = [(_get_type_proto_info(vi.type)) for vi in model.graph.output]
    return [vi.name for vi in model.graph.output], [e[0] for e in type_info], [e[1] for e in type_info]


## Methods for read test data ##

def _check_type_and_size(obj, size):
    if obj is None:
        return size
    elif isinstance(obj, (list, tuple)) and (size == 0 or size == len(obj)):
        return len(obj)
    else:
        raise RuntimeError("Invalid params {} with expect size {}".format(obj, size))


# Read data from txt file(default dtype: float32)
# Return: List(Tuple) [(k1,v1), (k2,v2), ...]
def get_data_txt(filepath, names = None, shape = None, dtype = None):

    def _get_data(f, s, dt):
        line = next(f)  # fin.readline()
        d = line.strip().strip(",").split(",")
        if d == [""]: raise StopIteration
        d = np.array(d).astype(dt)
        return d.reshape([-1,] + s[1:]) if s else d

    # check names, dtype and shape
    size = _check_type_and_size(names, 0)
    size = _check_type_and_size(dtype, size)
    size = _check_type_and_size(shape, size)
    size = size if size else 1
    # set default value
    if not names:
        names = [None] * size
    if not dtype:
        dtype = ["float32"] * size
    if not shape:
        shape = [None] * size

    with open(filepath, "r") as fin:
        while True:
            yield [(n, _get_data(fin, s, dt)) for n, s, dt in zip(names, shape, dtype)]


# data_feed: List(Tuple) [(k1,v1), (k2,v2), ...]
def _check_data_npz(data_feed, names = None, shape = None, dtype = None):
    func_check_shape = lambda x, y: len(x) == len(y) and all([s1 == s2 or 0 == s1 * s2 for s1, s2 in zip(x, y)])
    # Suppose input data order is consistent
    if names:
        data_names = [k for (k, _) in data_feed]
        assert(set(data_names) == set(names)), "{} != {}".format(data_names, names)
        data_dict = {k: v for (k, v) in data_feed}
        # reorder data accroding to input names
        data_feed = [(k, data_dict[k]) for k in names]
    if shape:
        for (_, v), s in zip(data_feed, shape):
            assert(func_check_shape(v.shape, s)), "{} != {}".format(v.shape, s)
    if dtype:
        for (_, v), dt in zip(data_feed, dtype):
            assert(v.dtype == dt), "{} != {}".format(v.dtype, dt)
    return data_feed


# Read data from npz file
# Return: List(Tuple) [(k1,v1), (k2,v2), ...]
def get_data_npz(filepath, names = None, shape = None, dtype = None):
    # check names, dtype and shape
    size = _check_type_and_size(names, 0)
    size = _check_type_and_size(dtype, size)
    size = _check_type_and_size(shape, size)

    data_feed = [] # List(Tuple)
    data_npz = np.load(filepath, allow_pickle=False)
    for name, data in data_npz.items():
        data_feed.append((name, data))
        if len(data_feed) == size:
            yield _check_data_npz(data_feed, names, shape, dtype)
            data_feed = []
        elif size == 0:
            yield data_feed
            data_feed = []
        else:
            pass
    raise StopIteration


def get_data_npz_pickle(filepath, names = None, shape = None, dtype = None):
    # check names, dtype and shape
    size = _check_type_and_size(names, 0)
    size = _check_type_and_size(dtype, size)
    size = _check_type_and_size(shape, size)

    data_npz = np.load(filepath, allow_pickle=True)
    for _, v in data_npz.items():
        data_feed = v.reshape((-1))[0] # <class 'dict'>
        if size:
            assert(len(data_feed) == size), "{} != {}".format(len(data_feed), size)
        yield _check_data_npz(data_feed, names, shape, dtype)
    raise StopIteration


def get_data_loader(filepath, names = None, shape = None, dtype = None):
    if filepath.endswith(".txt"):
        return get_data_txt(filepath, names, shape, dtype)
    if filepath.endswith(".npz"):
        return get_data_npz_pickle(filepath, names, shape, dtype) if npz_with_pickle else get_data_npz(filepath, names, shape, dtype)
    raise RuntimeError("Unsupport data file format {}".format(filepath))


## Methods for checking consistency ##

def check_output_tol(desired, actual, atol, rtol, diff_max = False, verbose = 0):
    assert(len(desired) == len(actual)), "desired output count {} != actual output count {}".format(len(desired), len(actual))
    for (n1, o1), (n2, o2) in zip(desired, actual):
        # check name
        if n1 and n2:
            assert(n1 == n2), "desired output name {} != actual output name {}".format(n1, n2)
        # check ndim and shape
        if o1.ndim != 1 and o2.ndim != 1:
            assert(o1.shape == o2.shape), "desired output shape {} != actual output shape {}".format(o1.shape, o2.shape)
        else:
            mod = lambda x, y: x % y if x > y else y % x
            assert(0 == mod(o1.size, o2.size)), "desired output shape {} isn't compatible with actual output shape {}".format(o1.shape, o2.shape)
            # flatten to 1-dim array
            if o1.ndim != 1:
                o1 = o1.reshape((-1))
            if o2.ndim != 1:
                o2 = o2.reshape((-1))
        # check tolerance
        if diff_max:
            np.testing.assert_allclose(o2, o1, atol=atol, rtol=rtol)
            if verbose > 1:
                print("{} desired output {}".format(n1, o1))
                print("{}  actual output {}".format(n2, o2))
    if not diff_max:
        #diff_abs = [np.abs(a-e) for (_, a), (_, e) in zip(actual, desired)]
        #print(len(diff_abs))
        diff_abs_avg = [np.average(np.abs(a-e)) for (_, a), (_, e) in zip(actual, desired)]
        diff_abs_max = [np.max(np.abs(a-e)) for (_, a), (_, e) in zip(actual, desired)]
        print("average abs diff:", diff_abs_avg)
        print("maximum abs diff:", diff_abs_max)


def show_output_tol(desired, actual, atol, rtol):
    assert(len(desired) == len(actual)), "desired output count {} != actual output count {}".format(len(desired), len(actual))
    for (n1, o1), (n2, o2) in zip(desired, actual):
        diff_abs = np.abs(o1 - o2)
        diff_idx = np.where(diff_abs > atol)
        if 0 < len(diff_idx):
            print("maximum abs diff > {} count: {}".format(atol, len(diff_idx[0])))
            print("{} desired output {}".format(n1, o1[diff_idx]))
            print("{}  actual output {}".format(n2, o2[diff_idx]))


class OnnxModelInfo(ABC):

    def __init__(self, targets, path, intra_threads = 0, inter_threads = 0, check_model = True):
        self._path = path
        self._model_proto = onnx.load(path)
        if check_model:
            onnx.checker.check_model(self._model_proto)

        # input/output names/shape/dtype
        _clean_initializers(self._model_proto)
        self._input_names, self._input_dtype, self._input_shape = _get_input_value_info(self._model_proto)
        self._output_names, self._output_dtype, self._output_shape = _get_output_value_info(self._model_proto)

        # ==========================
        # Config ort session options
        # ==========================
        self._sess_opt = rt.SessionOptions()
        # Set thread number and working mode
        self._sess_opt.intra_op_num_threads = intra_threads
        self._sess_opt.inter_op_num_threads = inter_threads
        #self._sess_opt.execution_mode = rt.ExecutionMode.ORT_SEQUENTIAL
        # Set graph optimization level
        #self._sess_opt.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_EXTENDED

        # create runtime session
        self._providers = [constant_to_provider_map[ep] for ep in targets]
        self._session = rt.InferenceSession(path, self._sess_opt, providers=self._providers)

    def __del__(self):
        pass

    def __call__(self, input_feed, run_options = None):
        sess_output = self._session.run(self._output_names, input_feed=input_feed, run_options=run_options)
        return sess_output

    def __str__(self, sep = "\n"):
        self._str = [
            "Input tensor (name, shape, dtype):",
            sep.join(["  {} {} {}".format(n, s, d) for n, s, d in zip(self._input_names, self._input_shape, self._input_dtype)]),
            "Output tensor (name, shape, dtype):",
            sep.join(["  {} {} {}".format(n, s, d) for n, s, d in zip(self._output_names, self._output_shape, self._output_dtype)]),
        ]
        return sep.join(self._str)

    def to_str(self, sep = "\n"):
        return self.__str__(sep)

    __repr__ = __str__


def get_data_runtime(args):
    # Env settings
    if args.verbose > 1:
        # Sets the default logging severity. 0:Verbose, 1:Info, 2:Warning, 3:Error, 4:Fatal
        rt.set_default_logger_severity(0)
        # Sets the default logging verbosity level. To activate the verbose log,
        # you need to set the default logging severity to 0:Verbose level. Default = 0. Valid values are >=0.
        rt.set_default_logger_verbosity(0)

    # Create onnx models info instance
    omi = OnnxModelInfo(args.target, args.model, args.intra_threads, args.inter_threads)

    # Show verbose info
    if args.verbose:
        print("Load onnx model from \"{}\"".format(args.model))
        print("Input Providers: {}{}{}".format(omi._providers, sep, omi.to_str(sep)))

    # Prepare test data loader function (with shape/dtype from input onnx model)
    input_names, input_shape, input_dtype = omi._input_names, omi._input_shape, omi._input_dtype
    data_loader_runtime = get_data_loader(args.input, input_names, input_shape, input_dtype)

    while True:
        input_data = next(data_loader_runtime)
        input_feed = {k : v for (k, v) in input_data}
        output = omi(input_feed)
        yield [(k, v) for k, v in zip(omi._output_names, output)]


def check_precision(args):
    # Prepare data loader for expected output data
    data_loader_desired = get_data_loader(args.desired)

    if args.actual:
        # Prepare data loader for Case1(with actual output)
        data_loader_actual = get_data_loader(args.actual)
    else:
        # Prepare data loader for Case2(with input data and onnx model)
        data_loader_actual = get_data_runtime(args)

    from functools import reduce
    elem_size = lambda output: reduce(lambda x, y: x + y, [arr.size for (_, arr) in output])
    while True:
        try:
            output_actual, output_desired = None, None
            output_desired = next(data_loader_desired)
            output_actual = next(data_loader_actual)
            output_desired_size = elem_size(output_desired)
            output_actual_size = elem_size(output_actual)
            # load same output elements is necessary
            if output_desired_size < output_actual_size:
                while output_desired_size < output_actual_size:
                    output_once_more = next(data_loader_desired)
                    output_desired.extend(output_once_more)
                    output_desired_size += elem_size(output_once_more)
            elif output_actual_size < output_desired_size:
                while output_actual_size < output_desired_size:
                    output_once_more = next(data_loader_actual)
                    output_actual.extend(output_once_more)
                    output_actual_size += elem_size(output_once_more)
            #print("output desired size: {}, data: {}".format(output_desired_size, output_desired))
            #print("output  actual size: {}, data: {}".format(output_actual_size, output_actual))
            assert(output_actual_size == output_desired_size), "{} != {}".format(output_actual_size, output_desired_size)
            # check desired and actual outputs
            check_output_tol(output_desired, output_actual, args.atol, args.rtol, args.diff_max, args.verbose)
        except StopIteration:
            print("check fin")
            break
        except AssertionError:
            if output_desired and output_actual:
                show_output_tol(output_desired, output_actual, args.atol, args.rtol)
            #break
        except RuntimeError:
            import traceback
            if "StopIteration" in traceback.format_exc():
                print("check fin")
                break
            else:
                traceback.print_exc()
        except Exception:
            import traceback
            traceback.print_exc()
    return 0


def main():
    parser = get_argsparser_precision(epilog=_HELP_TEXT)
    args = parser.parse_args()

    if not args.actual and not (args.model and args.input):
        parser.print_help()
        sys.exit(1)
    return check_precision(args)


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == '#%s' % magic:
        del sys.argv[-1]
    if "--gdb" in sys.argv:
        sys.argv.remove("--gdb")
    sys.exit(main())


del magic
