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
# Brief:  Toolkit to convert onnx graphs to JDSK model format

# shell code:
#"""eval" set -xe """#"

# python code:
magic='--calling-python-from-/bin/bash--'
"""exec" $([[ $* =~ --gdb ]] && echo "gdb --args") python3 "$0" "$@" """#$magic"

# pylint: disable=unused-argument,unused-import,ungrouped-imports,wrong-import-position

_HELP_TEXT_ONNX = """
Usage Examples:

# Convert dynamic graph to static graph with '--inputs name1[shape1],name2[shape2],...'
python3 -m onnx2jdsk --input frozen_graph.onnx --output frozen_graph_static.onnx --inputs A[1,3,64,64]
# Convert dynamic graph to static graph with '-f name:value' or '-F denotation:value'
python3 -m onnx2jdsk --input frozen_graph.onnx --output frozen_graph_static.onnx -f Dim1:10 -F DATA_CHANNEL:20
"""

def _check_args(args):
    parse_dimension_override = lambda kv_list: {e.rsplit(":", 1)[0] : e.rsplit(":", 1)[1] for e in kv_list}
    args.free_dim_param = parse_dimension_override(args.free_dim_param) if len(args.free_dim_param) else {}
    args.free_dim_denotation = parse_dimension_override(args.free_dim_denotation) if len(args.free_dim_denotation) else {}
    return args


def convert(args):
    args = _check_args(args)

    import onnx
    from jdsk.utils import get_input_output_names, split_nodename_and_shape
    # Load onnx model
    onnx_model = onnx.load(args.input)
    input_names, output_names = get_input_output_names(onnx_model)

    input_names_override, output_names_override = None, None
    input_shape_override, output_shape_override = None, None
    if args.inputs:
        input_names_override, input_shape_override = split_nodename_and_shape(args.inputs)
    if args.outputs:
        output_names_override, output_shape_override = split_nodename_and_shape(args.outputs)

    # Experimental: extract subgraph if required
    if (input_names_override and sorted(input_names_override) != sorted(input_names)) or \
        (output_names_override and sorted(output_names_override) != sorted(output_names)):
        # check onnx version
        _ver = onnx.__version__.split(".")
        if int(_ver[0]) < 1 or int(_ver[1]) < 8:
            raise RuntimeError("onnx.utils.Extractor only available since v1.8.0, while runtime onnx version is {}".format(onnx.__version__))
        # extract subgraph
        e = onnx.utils.Extractor(onnx_model)
        if not input_names_override:
            input_names_override = input_names
        if not output_names_override:
            output_names_override = output_names
        if args.verbose:
            print(" Input tensor names override:", input_names_override)
            print("Output tensor names override:", output_names_override)
        onnx_model = e.extract_model(input_names_override, output_names_override)

    # Experimental: override input/output shape if required
    if input_shape_override or output_shape_override:
        if args.verbose:
            print(" Input tensor shape override:", input_shape_override)
            print("Output tensor shape override:", output_shape_override)
        # Override input/output node shape dimension
        from jdsk.utils import update_inputs_outputs_dims
        onnx_model = update_inputs_outputs_dims(onnx_model, input_shape_override, output_shape_override)
    if len(args.free_dim_param) or len(args.free_dim_denotation):
        if args.verbose:
            print("Free dimension override by name:", args.free_dim_param)
            print("Free dimension override by denotation", args.free_dim_denotation)
        from jdsk.utils import override_free_dimensions
        onnx_model = override_free_dimensions(onnx_model, args.free_dim_param, args.free_dim_denotation)

    onnx.save(onnx_model, args.output)
    if args.onnxsim:
        from onnxsim import simplify
        onnx_model, check = simplify(onnx_model)
        if check:
            onnx.save(onnx_model, args.output)
        else:
            print("[WARN] simplify the onnx model with onnxsim failed!")
    if args.checker:
        onnx.checker.check_model(args.output)


def main():
    from jdsk.converter.argsparser import get_argsparser_onnx
    parser = get_argsparser_onnx(epilog=_HELP_TEXT_ONNX)
    convert(parser.parse_args())


if __name__ == "__main__":
    import sys, os
    if sys.argv[-1] == '#%s' % magic:
        del sys.argv[-1]
    if "--gdb" in sys.argv:
        sys.argv.remove("--gdb")

    parent = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent, "..", ".."))
    main()


del magic
