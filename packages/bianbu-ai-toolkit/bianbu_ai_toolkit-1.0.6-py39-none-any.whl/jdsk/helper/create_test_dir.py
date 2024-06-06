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
# Brief:  Commandline tool to create test dir for input model
# History:
# 2023/12/04  v0.0.1  init/create

import os
import argparse
import numpy as np
import onnx
from onnx import numpy_helper
try:
    from onnx.helper import tensor_dtype_to_np_dtype
    to_np_type = lambda x: tensor_dtype_to_np_dtype(x)
except:
    from onnx.mapping import TENSOR_TYPE_TO_NP_TYPE
    to_np_type = lambda x: TENSOR_TYPE_TO_NP_TYPE[x]
from onnx import onnx_pb

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

import string
letters = list(string.ascii_lowercase + string.digits)
# Func to generate random data
rand_int = lambda low, high, shape, dtype: np.random.randint(int(low), int(high), size=shape, dtype=dtype)
rand_str = lambda low, high, shape, dtype: np.random.choice(letters, size=shape, replace=True)
rand_fp = lambda low, high, shape, dtype: (np.random.random(size=shape) * (high - low) + low).astype(dtype)
rand_data = lambda low, high, shape, dtype: \
    rand_int(low, high, shape, dtype) if 'int' in dtype else \
    (rand_str(low, high, shape, dtype) if "string" == dtype else rand_fp(low, high, shape, dtype))


def get_argsparser_tensor_proto(parser = None, epilog = None):
    """Parse commandline."""
    if parser is None:
        parser = argparse.ArgumentParser(description="Toolkit to create test dir for input model.",
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("--model_path", "-m", type=str, required=True, help="Path to the onnx model file to use.")
    parser.add_argument("--root_path", "-d", type=str, required=True, help="Root path to create the test directory in.")
    parser.add_argument("--test_name", "-n", type=str, required=True, help="Name for test. Will be added to the root_path to create the test directory name.")
    parser.add_argument("--repeat", "-r", type=int, default=1, help="Repeat times.")
    # Args for input shape(s)
    parser.add_argument("--inputs", type=str, help="input tensor shape override for testing")
    parser.add_argument("--outputs", type=str, help="output tensor shape override for testing(ignored at present)")
    parser.add_argument("--free_dim_param", "-f", type=str, nargs='+', default=[], help="[dimension_name:override_value] specify a value(must > 0) to override a free dimension by name(dim.dim_param).")
    parser.add_argument("--free_dim_denotation", "-F", type=str, nargs='+', default=[], help="[dimension_denotation:override_value] specify a value(must > 0) to override a free dimension by denotation(dim.denotation).")
    # Args for test data
    parser.add_argument("--val_high", "-vh", type=float, default=1.0, help="maximum test data value(default: 1.0)")
    parser.add_argument("--val_low", "-vl", type=float, default=0.0, help="minimum test data value(default: 0.0)")
    # Args for output(s)
    parser.add_argument("--formats", type=str.lower, nargs='+', default=["pb"], choices=["pb", "npz"], help="Output tensor file type.")
    parser.add_argument("--save_output", default=False, help="Save output or not", action='store_true')
    return parser


def _get_numpy_type(model_info, name):
    for i in model_info:
        if i.name == name:
            type_name = i.type.WhichOneof("value")
            if type_name == "tensor_type":
                return to_np_type(i.type.tensor_type.elem_type)
            else:
                raise ValueError(f"Type is not handled: {type_name}")

    raise ValueError(f"{name} was not found in the model info.")


def _create_missing_input_data(
        model_inputs,
        shape_override,
        symbolic_dim_values_map,
        denotation_dim_values_map,
        initializer_set,
        val_high=10.0, val_low=-10.0
    ):
    """
    Update name_input_map with random input for any missing values in the model inputs.

    :param model_inputs: model.graph.input from an onnx model
    :param symbolic_dim_values_map: Map of symbolic dimension names to values to use if creating data.
    :param denotation_dim_values_map: Map of denotation dimension names to values to use if creating data.

    :return: Map of input names to values to update. Can be empty. Existing values are preserved.
    """
    def _get_dims_from_tensor_type(tensor_type):
        shape = tensor_type.shape
        dims = []
        for dim in shape.dim:
            dim_type = dim.WhichOneof("value")
            if dim_type == "dim_value":
                dims.append(dim.dim_value)
            elif dim_type == "dim_param":
                if dim.dim_param not in symbolic_dim_values_map:
                    if dim.HasField("denotation") and dim.denotation in denotation_dim_values_map:
                        dims.append(int(denotation_dim_values_map[dim.denotation]))
                    else:
                        raise ValueError(f"Value for symbolic dim {dim.dim_param} was not provided.")
                else:
                    dims.append(int(symbolic_dim_values_map[dim.dim_param]))
            else:
                # TODO: see if we need to provide a way to specify these values. could ask for the whole
                # shape for the input name instead.
                raise ValueError("Unsupported model. Unknown dim with no value or symbolic name.")
        return dims

    name_input_map = {}
    for input in model_inputs:
        # skip if the input has already exists in initializer
        # models whose ir_version < 4 can have input same as initializer; no need to create input data
        if input.name in initializer_set:
            continue
        input_type = input.type.WhichOneof("value")
        if input_type != "tensor_type":
            raise ValueError(f"Unsupported model. Need to handle input type of {input_type}")

        dims = shape_override[input.name] if input.name in shape_override else _get_dims_from_tensor_type(input.type.tensor_type)

        # create random data. give it range -10 to 10 so if we convert to an integer type it's not all 0s and 1s
        #np_type = to_np_type(input.type.tensor_type.elem_type)
        #data = (np.random.standard_normal(dims) * 10).astype(np_type)
        data = rand_data(val_low, val_high, dims, ONNX_DTYPE_NAMES[input.type.tensor_type.elem_type])

        name_input_map[input.name] = data

    return name_input_map


def create_test_dir(
    model_path, test_data_dir, shape_override=None,
    symbolic_dim_values_map=None, denotation_dim_values_map=None,
    val_high=10.0, val_low=-10.0, formats=["pb"], save_output=False,
):
    """
    Create a test directory that can be used with onnx_test_runner or onnxruntime_perf_test.
    Generates random input data for any missing inputs.

    :param model_path: Path to the onnx model file to use.
    :param test_data_dir: Dir for test data. Will be added to the root_path.
    :param symbolic_dim_values_map: Map of symbolic dimension names to values to use for the input data if creating
                                    using random data.
    :param denotation_dim_values_map: Map of denotation dimension names to values to use for the input data if creating
                                    using random data.
    :return: None
    """

    model = onnx.load(model_path)
    model_inputs = model.graph.input
    model_outputs = model.graph.output

    def save_data(prefix, name_data_map, model_info, formats=["pb"], npz_with_pickle=False):
        if "npz" in formats:
            filename = os.path.join(test_data_dir, f"{prefix}.npz")
            np.savez_compressed(filename, **name_data_map if not npz_with_pickle else name_data_map)
        if "pb" not in formats:
            return
        idx = 0
        for name, data in name_data_map.items():
            if isinstance(data, dict):
                # ignore. map<T1, T2> from traditional ML ops
                pass
            elif isinstance(data, list):
                # ignore. vector<map<T1,T2>> from traditional ML ops. e.g. ZipMap output
                pass
            else:
                np_type = _get_numpy_type(model_info, name)
                tensor = numpy_helper.from_array(data.astype(np_type), name)
                filename = os.path.join(test_data_dir, f"{prefix}_{idx}.pb")
                with open(filename, "wb") as f:
                    f.write(tensor.SerializeToString())
            idx += 1

    if not shape_override:
        shape_override = {}
    if not symbolic_dim_values_map:
        symbolic_dim_values_map = {}
    if not denotation_dim_values_map:
        denotation_dim_values_map = {}
    initializer_set = set()
    for initializer in onnx.load(model_path).graph.initializer:
        initializer_set.add(initializer.name)
    name_input_map = _create_missing_input_data(
        model_inputs, shape_override,
        symbolic_dim_values_map, denotation_dim_values_map,
        initializer_set, val_high=val_high, val_low=val_low)
    save_data("input", name_input_map, model_inputs, formats=formats)

    # save expected output data if provided. run model to create if not.
    if save_output:
        import onnxruntime as ort
        output_names = [o.name for o in model_outputs]
        sess = ort.InferenceSession(model_path)
        outputs = sess.run(output_names, name_input_map)
        name_output_map = {}
        for name, data in zip(output_names, outputs):
            name_output_map[name] = data
        save_data("output", name_output_map, model_outputs, formats=formats)


def create_test_data(args):
    assert(args.val_high >= args.val_low), "Invalid value high {} < value low {}".format(args.val_high, args.val_low)
    # parse free dim param/denotation
    assert(all([":" in e for e in args.free_dim_param])), "Invalid free_dim_param: {}".format(args.free_dim_param)
    assert(all([":" in e for e in args.free_dim_denotation])), "Invalid free_dim_denotation: {}".format(args.free_dim_denotation)
    parse_dimension_override = lambda kv_list: {e.rsplit(":", 1)[0] : e.rsplit(":", 1)[1] for e in kv_list}
    symbolic_dim_values_map = parse_dimension_override(args.free_dim_param) if len(args.free_dim_param) else {}
    denotation_dim_values_map = parse_dimension_override(args.free_dim_denotation) if len(args.free_dim_denotation) else {}
    assert(all([v.isdecimal() for _, v in symbolic_dim_values_map.items()]))
    assert(all([v.isdecimal() for _, v in denotation_dim_values_map.items()]))

    model_path = os.path.abspath(args.model_path)
    root_path = os.path.abspath(args.root_path)
    test_dir = os.path.join(root_path, args.test_name)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    model_filename = os.path.split(model_path)[-1]
    test_model_filename = os.path.join(test_dir, model_filename)
    import shutil
    # always override
    shutil.copy(model_path, test_model_filename)

    # Override input shape
    from jdsk.utils import split_nodename_and_shape
    (_, shape_override) = split_nodename_and_shape(args.inputs) if args.inputs else (None, None)

    # add to existing test data sets if present
    test_num = 0
    for _ in range(args.repeat):
        while True:
            test_data_dir = os.path.join(test_dir, "test_data_set_" + str(test_num))
            if not os.path.exists(test_data_dir):
                os.mkdir(test_data_dir)
                break
            test_num += 1
        try:
            create_test_dir(
                test_model_filename, test_data_dir, shape_override,
                symbolic_dim_values_map, denotation_dim_values_map,
                val_high=args.val_high, val_low=args.val_low,
                formats=args.formats, save_output=args.save_output,
            )
            print("[INFO] create random test data under {} done".format(test_data_dir))
        except Exception as e:
            #print(e)
            import traceback
            traceback.print_exc()
            print("[INFO] create random test data under {} fail".format(test_data_dir))
            if os.path.exists(test_data_dir):
                shutil.rmtree(test_data_dir)
            break


def main():
    parser = get_argsparser_tensor_proto(epilog="")
    args = parser.parse_args()
    create_test_data(args)


if __name__ == "__main__":
    import sys
    parent = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent, "..", ".."))
    main()