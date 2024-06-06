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
# Brief:  Toolkit to convert caffe model to JDSK model format

# pylint: disable=unused-argument,unused-import,ungrouped-imports,wrong-import-position

_HELP_TEXT_CAFFE = """
Usage Examples:

$ python -m caffe2jdsk --input lenet --output lenet.onnx
"""

def _check_args(args):
    return args


# TODO: Try to support to convert caffe2 to onnx
# https://github.com/onnx/tutorials/blob/master/tutorials/Caffe2OnnxExport.ipynb


# Convert caffe model to onnx, which based on:
# https://github.com/onnx/onnx-docker/blob/master/onnx-ecosystem/converter_scripts/caffe_coreml_onnx.ipynb
def convert(args):
    args = _check_args(args)

    proto_file = ".".join([args.input, "prototxt"])
    model_file = ".".join([args.input, "caffemodel"])

    import coremltools
    import onnxmltools

    # Convert Caffe model to CoreML
    coreml_model = coremltools.converters.caffe.convert((model_file, proto_file))

    if args.verbose:
        coreml_tmp = args.output.replace(".onnx", ".mlmodel")
        # Save CoreML model
        coreml_model.save(coreml_tmp)
        # Load a CoreML model
        coreml_model = coremltools.utils.load_spec(coreml_tmp)

    # Convert the CoreML model to ONNX
    onnx_model = onnxmltools.convert_coreml(coreml_model)
    onnxmltools.utils.save_model(onnx_model, args.output)


def main():
    from jdsk.converter.argsparser import get_argsparser_caffe
    parser = get_argsparser_caffe(epilog=_HELP_TEXT_CAFFE)
    convert(parser.parse_args())


if __name__ == "__main__":
    import sys, os
    parent = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent, "..", ".."))
    main()
