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
# Brief:  Toolkit to test onnx model with onnxruntime

# shell code:
#"""eval" set -xe """#"

# CUDA settings
#"""eval" export CUDA_VISIBLE_DEVICES=0 """#"

# python code:
magic='--calling-python-from-/bin/bash--'
"""exec" $([[ $* =~ --gdb ]] && echo "gdb --args") python3 "$0" "$@" """#$magic"

# pylint: disable=unused-argument,unused-import,ungrouped-imports,wrong-import-position

import argparse
import time
from abc import ABC, abstractmethod
import onnx
import onnxruntime as rt
import numpy as np

__version__ = "0.0.2"

_HELP_TEXT = """
Usage Examples:

# test with specific providers
python3 -m onnx2jdsk.test --input model.onnx --target xnnpack cpu
# test and save output to file
python3 -m onnx2jdsk.test --input model.onnx --output output.txt
# test with prepared input data
python3 -m onnx2jdsk.test --input model.onnx --in_data in_data.txt
# test dynamic graph with random batch size
python3 -m onnx2jdsk.test --input model.onnx --min_batch_size 1 --max_batch_size 10
# test and check outputs between models(with same input/output names/shape/dtype)
python3 -m onnx2jdsk.test --input model1.onnx --input2 model2.onnx --atol 1e-4 --rtol 1e-3 --diff_max -v
"""

sep = "\n"
npz_with_pickle = False

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

# predefined meta function for opaque input shape dimension
meta_func = {
    '#': lambda *args : len(args),
    '0': lambda *args : args[0], # identity mapping with 1st input parameter
    '1': lambda *args : args[1], # identity mapping with 2nd input parameter
    '2': lambda *args : args[0] * args[1],
}


def get_argsparser_test(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to test onnx model with onnxruntime(version {}).".format(__version__),
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    # Args for quick testing onnxruntime
    parser.add_argument("--input", type=str, required=True, help="input model file path")
    parser.add_argument("--output", type=str, default=None, help="output data file path")
    parser.add_argument("--target", type=str.lower, nargs='+', default=['cpu'], choices=meta_bkds, help="target platform(s), aka provider(s)")
    parser.add_argument("--in_data", type=str, default=None, help="input test data file path")
    parser.add_argument("--err_data", type=str, default=None, help="error test data file path")
    parser.add_argument("--eval_round", "-er", type=int, default=100, help="test round")
    parser.add_argument("--intra_threads", type=int, default=0, help="intra_op_num_threads of onnxruntime session options")
    parser.add_argument("--inter_threads", type=int, default=0, help="inter_op_num_threads of onnxruntime session options")
    parser.add_argument("--val_high", "-vh", type=float, default=1.0, help="maximum test data value(default: 1.0)")
    parser.add_argument("--val_low", "-vl", type=float, default=0.0, help="minimum test data value(default: 0.0)")
    # Args for dynamic graph
    parser.add_argument("--inputs", type=str, help="input tensor shape override for testing")
    parser.add_argument("--outputs", type=str, help="output tensor shape override for testing(ignored at present)")
    parser.add_argument("--free_dim_param", "-f", type=str, nargs='+', default=[], help="[dimension_name:override_value] specify a value(must > 0) to override a free dimension by name(dim.dim_param).")
    parser.add_argument("--free_dim_denotation", "-F", type=str, nargs='+', default=[], help="[dimension_denotation:override_value] specify a value(must > 0) to override a free dimension by denotation(dim.denotation).")
    parser.add_argument("--max_batch_size", type=int, default=20, help="maximum batch size for testing dynamic graph(default: 20)")
    parser.add_argument("--min_batch_size", type=int, default=1, help="minimum batch size for testing dynamic graph(default: 1)")
    parser.add_argument("--meta_shape", type=str, default=None,
                        help="Meta function description for symbolic tensor shape or shape dimension value(integer) which <=0. Currently, "
                        "at most one such opaque dimension in each shape could be supported. In such case, the dimension value will be "
                        "computed as meta_func[idx](*args). The default meta funtion(i.e. meta_func[0]) is just like identity mapping "
                        "f(*args): *args -> args[0], while args[0] is the dynamic random max_batch_size for the most time. For example, "
                        "--meta_shape 1:2,3:1 means both input_shape[1] and input_shape[3] have an opaque dimension, and they should "
                        "be computed as meta_func['2'](*args) = args[0] * args[1] and meta_func['1'](*args) = args[1] respectively.")
    parser.add_argument("--meta_data", type=str, default=None,
                        help="Meta data/arguments for meta function used in opaque dimension(e.g. symbolic tensor shape). For example, "
                        "--meta_shape 1:2,3:1 --meta_data 1:8,3:4 means both input_shape[1] and input_shape[3] have an opaque dimension, "
                        "and input_shape[1] should be computed as meta_func['2'](*args) = args[0] * args[1], where args[0] is actually the "
                        "max_batch_size, and args[1] is '8' which specified in '--meta_data'.")
    # Args for debugging
    parser.add_argument("--verbose", "-v", default=0, help="additive option, "
                                                           "-v: show verbose model info and save exception test data, "
                                                           "-vv: print model outputs", action="count")
    # Args for checking consistency between two models
    parser.add_argument("--input2", type=str, default=None, help="model2 input file path")
    parser.add_argument("--output2", type=str, default=None, help="model2 output data file path")
    parser.add_argument("--target2", type=str.lower, nargs='+', default=['cpu'], choices=meta_bkds, help="model2 target platform(s), aka provider(s)")
    parser.add_argument("--diff_max", default=False, help="check maximum abs difference or not", action='store_true')
    parser.add_argument("--atol", type=float, default=1e-4, help="absolute tolerance(default: 1e-4)")
    parser.add_argument("--rtol", type=float, default=0, help="relative tolerance(default: 0)")
    return parser


def _check_args(args):
    parse_dimension_override = lambda kv_list: {e.rsplit(":", 1)[0] : e.rsplit(":", 1)[1] for e in kv_list}
    args.free_dim_param = parse_dimension_override(args.free_dim_param) if len(args.free_dim_param) else {}
    args.free_dim_denotation = parse_dimension_override(args.free_dim_denotation) if len(args.free_dim_denotation) else {}
    return args


## Methods for preparing test data ##

def prepare_runtime_shape(input_shape, args, **kwargs):
    """
    Return:
        input_shape runtime input shape
    """
    # TODO: assert input tensor with sequence<uint8[?,?,3]>
    func_indicator = lambda x : (isinstance(x, int) and 0 < x) or (isinstance(x, list) and all([isinstance(e, int) and 0 < e for e in x]))
    shape_indicator = [[func_indicator(s) for s in shape] for shape in input_shape]
    # Check input shape: Currently, at most one dimension in each shape could be an opaque dimension, i.e.
    # 1) string as "symbolic tensor shape" or 2) integer which value <= 0, which will always be replaced
    # by meta_func[idx](max_batch_size, ...), e.g. f(max_batch_size, ...) = max_batch_size.
    assert(all([True if i.count(False) < 2 else False for i in shape_indicator])), "unexpected dynamic shape {}".format(input_shape)

    if all([True if indicator.count(False) == 0 else False for indicator in shape_indicator]):
        # i.e. no opaque dimension is found, e.g. static graph
        while True:
            yield input_shape
    else:
        # i.e. at most one opaque dimension in each shape
        if args.verbose > 0:
            print("Input meta data for shape func:", args.meta_data)
        import re
        shape_pattern = re.compile(r"(?:([\d]+):([\d]+)?),?")
        shape_splits = re.split(shape_pattern, args.meta_shape) if args.meta_shape else []
        param_splits = re.split(shape_pattern, args.meta_data) if args.meta_data else []
        shape_func = {} # index -> lambda func
        shape_args = {} # index -> params list
        for i in range(1, len(shape_splits), 3):
            assert(shape_splits[i + 1])
            shape_func[int(shape_splits[i])] = meta_func[shape_splits[i + 1]]
        for i in range(1, len(param_splits), 3):
            assert(param_splits[i + 1])
            shape_args[int(param_splits[i])] = [int(param_splits[i + 1])]
        while True:
            _input_shape, _batch_size = [], np.random.randint(args.min_batch_size, args.max_batch_size + 1)
            for i, shape in enumerate(input_shape):
                _shape, meta_args = [], shape_args.setdefault(i, [])
                for s, b in zip(shape, shape_indicator[i]):
                    if isinstance(s, list):
                        _indicator = [func_indicator(_s) for _s in s]
                        _shape.append([_s if _b else shape_func.setdefault(i, meta_func['0'])( \
                            np.random.randint(args.min_batch_size, args.max_batch_size + 1), *meta_args) for _s, _b in zip(s, _indicator)])
                    else:
                        _shape.append(s if b else shape_func.setdefault(i, meta_func['0'])(_batch_size, *meta_args))
                _input_shape.append(_shape)
            yield _input_shape


def prepare_random_data(get_shape, input_dtype, args):
    # To support dtype 'string'
    import string
    letters = list(string.ascii_lowercase + string.digits)
    # Func to generate random data
    rand_int = lambda low, high, shape, dtype: np.random.randint(int(low), int(high), size=shape, dtype=dtype)
    rand_str = lambda low, high, shape, dtype: np.random.choice(letters, size=shape, replace=True)
    rand_fp = lambda low, high, shape, dtype: (np.random.random(size=shape) * (high - low) + low).astype(dtype)
    rand_data = lambda low, high, shape, dtype: \
        rand_int(low, high, shape, dtype) if 'int' in dtype else \
        (rand_str(low, high, shape, dtype) if "string" == dtype else rand_fp(low, high, shape, dtype))
    # Generate random test data
    input_data = []
    for i in range(args.eval_round):
        _input_shape = next(get_shape)
        assert(len(_input_shape) == len(input_dtype))
        # Generate/Update input tensor data.
        input_data[:len(_input_shape)] = [
            [rand_data(args.val_low, args.val_high, _s, _d) for _s, _d in zip(s, d)] if isinstance(d, list) else rand_data(args.val_low, args.val_high, s, d)
            for s, d in zip(_input_shape, input_dtype)
        ]
        yield input_data, len(_input_shape)


def prepare_txt_data(input_shape, input_dtype, input_file, input_names = None):
    assert(len(input_shape) == len(input_dtype))
    with open(input_file, "r") as fin:
        while True:
            input_data = []
            for s, d in zip(input_shape, input_dtype):
                line = next(fin) # fin.readline()
                line = line.strip().strip(",").split(",")
                if line == [""]: raise StopIteration
                input_data.append(np.array(line).reshape([-1,] + s[1:]).astype(d))
            #for data in input_data: print(data.shape, data.dtype)
            yield input_data, len(input_data)


# data_feed: <class 'dict'>
def _check_data_npz(data_feed, names, shape = None, dtype = None):
    # check data names
    data_names = [k for k in data_feed.keys()]
    assert(set(data_names) == set(names)), "{} != {}".format(data_names, names)
    # convert data dict to list
    data_feed = [data_feed[name] for name in names]
    # check data shape and type
    func_check_shape = lambda x, y: len(x) == len(y) and all([s1 == s2 or 0 == s1 * s2 for s1, s2 in zip(x, y)])
    if shape:
        for v, s in zip(data_feed, shape):
            assert(func_check_shape(v.shape, s)), "{} != {}".format(v.shape, s)
    if dtype:
        for v, dt in zip(data_feed, dtype):
            assert(v.dtype == dt), "{} != {}".format(v.dtype, dt)
    return data_feed


def prepare_npz_data(input_shape, input_dtype, input_file, input_names):
    assert(len(input_shape) == len(input_dtype))
    assert(len(input_shape) == len(input_names))
    input_data = {}
    data_npz = np.load(input_file, allow_pickle=False)
    for name, data in data_npz.items():
        input_data[name] = data
        if len(input_data.keys()) == len(input_names):
            input_data = _check_data_npz(input_data, input_names, input_shape, input_dtype)
            yield input_data, len(input_data)
            input_data = {}
    raise StopIteration


def prepare_npz_data_pickle(input_shape, input_dtype, input_file, input_names):
    assert(len(input_shape) == len(input_dtype))
    assert(len(input_shape) == len(input_names))
    data_npz = np.load(input_file, allow_pickle=True)
    for _, v in data_npz.items():
        input_data = v.reshape((-1))[0] # <class 'dict'> as input_feed
        input_data = _check_data_npz(input_data, input_names, input_shape, input_dtype)
        yield input_data, len(input_data)
    raise StopIteration


def save_data_to_file(path, data, model):
    fdata = open(path, model)
    for d in data:
        fdata.write("%s,\n" % (",".join(d.flatten().astype(str).tolist())))
    fdata.close()


def handle_error_data(path, input_data, input_names, mode):
    if not path or not input_data or not input_names:
        return
    # save error data to disk
    if path.endswith('.npz'):
        feeds = {i : d for i, d in zip(input_names, input_data)}
        np.savez_compressed(path, **feeds if not npz_with_pickle else feeds)
    else:
        save_data_to_file(path, input_data, mode)


## Methods for checking consistency between two models ##

def check_output_tol(output_1, output_2, atol, rtol, diff_max = False, verbose = 0):
    assert(len(output_1) == len(output_2))
    for o1, o2 in zip(output_1, output_2):
        assert(o1.shape == o2.shape), "model1 output shape {} != model2 output shape {}".format(o1.shape, o2.shape)
        if diff_max:
            np.testing.assert_allclose(o2, o1, atol=atol, rtol=rtol)
            if verbose > 1:
                print("model1 output:", o1)
                print("model2 output:", o2)
    if not diff_max:
        #diff_abs = [np.abs(a-e) for a, e in zip(output_2, output_1)]
        #print(len(diff_abs))
        diff_abs_avg = [np.average(np.abs(a-e)) for a, e in zip(output_2, output_1)]
        diff_abs_max = [np.max(np.abs(a-e)) for a, e in zip(output_2, output_1)]
        print("average abs diff:", diff_abs_avg)
        print("maximum abs diff:", diff_abs_max)


def show_output_tol(output_1, output_2, atol, rtol):
    # show details for atol(currently ignore rtol)
    for o1, o2 in zip(output_1, output_2):
        diff_abs = np.abs(o1 - o2)
        diff_idx = np.where(diff_abs > atol)
        if 0 < len(diff_idx):
            print("maximum abs diff > {} count: {}".format(atol, len(diff_idx[0])))
            print("model1 output:", o1[diff_idx])
            print("model2 output:", o2[diff_idx])


class OnnxModelInfo(ABC):

    def __init__(self, targets, path, output = None, sess_opt = None, free_dim_param = {}, free_dim_denotation = {}, check_model = True):
        self._path = path
        self._fout = open(output, "w") if output else None
        self._model_proto = onnx.load(path)
        self._sess_opt = sess_opt if sess_opt else rt.SessionOptions()
        # update onnx model with free dimension override
        if len(free_dim_param) or len(free_dim_denotation):
            print("[INFO] Free dimension override by name:", free_dim_param)
            print("[INFO] Free dimension override by denotation", free_dim_denotation)
            from jdsk.utils import override_free_dimensions
            self._model_proto = override_free_dimensions(self._model_proto, free_dim_param, free_dim_denotation)
        if check_model:
            onnx.checker.check_model(self._model_proto)

        # input/output names/shape/dtype
        from jdsk.utils import clean_initializers, get_input_value_info, get_output_value_info
        clean_initializers(self._model_proto)
        self._input_names, self._input_dtype, self._input_shape = get_input_value_info(self._model_proto)
        self._output_names, self._output_dtype, self._output_shape = get_output_value_info(self._model_proto)

        # Enable model serialization after graph optimization
        #self._sess_opt.optimized_model_filepath = path.replace(".onnx", "_opt.onnx")

        # create runtime session
        self._providers = [constant_to_provider_map[ep] for ep in targets]
        self._session = rt.InferenceSession(path, self._sess_opt, providers=self._providers)
        self._t_clock = 0 # as runtime time cost

    def __del__(self):
        if self._fout:
            self._fout.close()

    def __call__(self, input_feed, run_options = None):
        t_start = time.time()
        sess_output = self._session.run(self._output_names, input_feed=input_feed, run_options=run_options)
        self._t_clock += time.time() - t_start
        if self._fout:
            for data in sess_output:
                self._fout.write("%s,\n" % (",".join(data.flatten().astype(str).tolist())))
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


def test(args):
    args = _check_args(args)

    if args.verbose > 1:
        # Sets the default logging severity. 0:Verbose, 1:Info, 2:Warning, 3:Error, 4:Fatal
        rt.set_default_logger_severity(0)
        # Sets the default logging verbosity level. To activate the verbose log,
        # you need to set the default logging severity to 0:Verbose level. Default = 0. Valid values are >=0.
        rt.set_default_logger_verbosity(0)

    # Create shared onnxruntime session option
    sess_opt = rt.SessionOptions()
    # Reset log level for verbosity
    if args.verbose > 1:
        sess_opt.log_severity_level = 0
        sess_opt.log_verbosity_level = 0
    # Set thread number and execution mode
    sess_opt.intra_op_num_threads = args.intra_threads
    sess_opt.inter_op_num_threads = args.inter_threads
    #sess_opt.execution_mode = rt.ExecutionMode.ORT_SEQUENTIAL
    # Set graph optimization level
    #sess_opt.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
    # Set free dimension override
    for k, v in args.free_dim_param.items():
        if v.isdecimal():
            sess_opt.add_free_dimension_override_by_name(k, int(v))
    for k, v in args.free_dim_denotation.items():
        if v.isdecimal():
            sess_opt.add_free_dimension_override_by_denotation(k, int(v))

    # Create onnx models info instance
    omi_1 = OnnxModelInfo(args.target, args.input, args.output, sess_opt, args.free_dim_param, args.free_dim_denotation)
    omi_2 = OnnxModelInfo(args.target2, args.input2, args.output2, sess_opt, args.free_dim_param, args.free_dim_denotation) if args.input2 else None

    # Check input/output names, shape and dtype
    omi_1_str = omi_1.to_str(sep)
    omi_2_str = omi_2.to_str(sep) if args.input2 else None
    if args.input2 and omi_1_str != omi_2_str:
        msg = [
            "{} and {} have different input or output names/shape/dtype!".format(args.input, args.input2),
            "## {} ##{}{}".format(args.input, sep, omi_1_str),
            "## {} ##{}{}".format(args.input2, sep, omi_2_str),
        ]
        raise ValueError(sep.join(msg))
    if args.verbose:
        print("Load onnx model from \"{}\"".format(args.input))
        print("Input Providers: {}{}{}".format(omi_1._providers, sep, omi_1_str))
    if args.verbose and args.input2:
        print("Load onnx model from \"{}\"".format(args.input2))
        print("Input Providers: {}{}{}".format(omi_2._providers, sep, omi_2_str))

    # Prepare test data (with shape/dtype from input onnx model)
    input_names, input_shape, input_dtype = omi_1._input_names, omi_1._input_shape, omi_1._input_dtype
    # Override input shape
    from jdsk.utils import split_nodename_and_shape
    (_, shape_override) = split_nodename_and_shape(args.inputs) if args.inputs else (None, None)
    check_compatible = lambda x, y: not isinstance(x, int) or x < 1 or (isinstance(y, int) and y == x)
    if shape_override:
        for i, n in enumerate(input_names):
            if n in shape_override.keys():
                assert(len(input_shape[i]) == len(shape_override[n])), "{} != {}".format(input_shape[i], shape_override[n])
                assert(all([check_compatible(x, y) for x, y in zip(input_shape[i], shape_override[n])])), "{} and {} are not compatible".format(input_shape[i], shape_override[n])
                input_shape[i] = shape_override[n]
    # Prepare test data function
    if args.in_data:
        get_prepare_npz_func = lambda pickle: prepare_npz_data_pickle if pickle else prepare_npz_data
        prepare_test_data = get_prepare_npz_func(npz_with_pickle) if args.in_data.endswith('.npz') else prepare_txt_data
        get_test_data = prepare_test_data(input_shape, input_dtype, args.in_data, input_names)
    else:
        get_test_data = prepare_random_data(prepare_runtime_shape(input_shape, args), input_dtype, args)

    # Test onnx model
    eval_round = 0
    while True:
        try:
            output_1, output_2, input_data = None, None, None
            input_data, _ = next(get_test_data)
            input_feed = {i : d for i, d in zip(input_names, input_data)}
            output_1 = omi_1(input_feed)
            if args.input2:
                # run model2 and check outputs between model1 and model2
                output_2 = omi_2(input_feed)
                check_output_tol(output_1, output_2, args.atol, args.rtol, args.diff_max, args.verbose)
            eval_round += 1
        except StopIteration:
            print("test fin")
            break
        except AssertionError:
            if output_1 and output_2:
                show_output_tol(output_1, output_2, args.atol, args.rtol)
                # save error data to disk
                if args.in_data is None and args.err_data:
                    handle_error_data(args.err_data, input_data, input_names, "a" if args.verbose else "w")
            if input_data and args.verbose == 0:
                raise RuntimeError("test fail! test data shape {}".format(" ".join([str(d.shape) for d in input_data])))
            import traceback
            traceback.print_exc()
            break
        except RuntimeError:
            import traceback
            if "StopIteration" in traceback.format_exc():
                print("test fin")
                break
            else:
                # save error data to disk
                if args.in_data is None and args.err_data:
                    handle_error_data(args.err_data, input_data, input_names, "a" if args.verbose else "w")
                traceback.print_exc()
    if args.eval_round == eval_round:
        print("[INFO] Model1 {} round cost: {}s".format(args.eval_round, omi_1._t_clock if eval_round else 0))
        print("[INFO] Model1 average latency: {}ms".format((omi_1._t_clock / args.eval_round * 1000) if eval_round else 0))
    if args.eval_round == eval_round and args.input2:
        print("[INFO] Model2 {} round cost: {}s".format(args.eval_round, omi_2._t_clock if eval_round else 0))
        print("[INFO] Model2 average latency: {}ms".format((omi_2._t_clock / args.eval_round * 1000) if eval_round else 0))
    return 0 if args.eval_round == eval_round else 1


def main():
    parser = get_argsparser_test(epilog=_HELP_TEXT)
    return test(parser.parse_args())


if __name__ == "__main__":
    import sys, os
    if sys.argv[-1] == '#%s' % magic:
        del sys.argv[-1]
    if "--gdb" in sys.argv:
        sys.argv.remove("--gdb")

    parent = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent, "..", ".."))
    sys.exit(main())


del magic
