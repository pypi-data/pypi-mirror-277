#!/bin/bash
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
# Brief:  Commandline tool to have a quick glance at onnx/tensorflow/pytorch/paddle/... model
# History:
# 2023/09/12  v0.0.1  init/create

# shell code:
#"""eval" set -xe """#"

# Set JDSK SDK Path
"""eval" export WORKSPACE=$(pwd) """#"
"""eval" export PYTHONPATH=$WORKSPACE/python:${PYTHONPATH} """#"
"""eval" export LD_LIBRARY_PATH=$WORKSPACE/lib:${LD_LIBRARY_PATH} """#"

# python code:
magic='--calling-python-from-/bin/bash--'
"""exec" python3 "$0" "$@" """#$magic"

# pylint: disable=unused-argument,unused-import,ungrouped-imports,wrong-import-position

import os, sys
import argparse
from abc import ABC, abstractmethod

# pylint: disable=unused-argument

__version__ = "0.0.1"

_HELP_TEXT = """
examples:
  python3 {fname} --onnx frozen.onnx -si -so -sn
  python3 {fname} --graphdef frozen.pb -si -so -sn
""".format(fname=os.path.basename(__file__))

def _not_implemented(*args):
    raise NotImplementedError("Sorry, not implement yet.")


class IHelper(ABC):

    def __init__(self, filepath):
        self._filepath = filepath

    def __call__(self, *args):
        return _not_implemented(*args)

    @abstractmethod
    def show_discription(self):
        return _not_implemented()

    @abstractmethod
    def show_nodes(self):
        return _not_implemented()

    @abstractmethod
    def show_inputs(self):
        return _not_implemented()

    @abstractmethod
    def show_outputs(self):
        return _not_implemented()

    @abstractmethod
    def to_external_data(self, filepath = None, location = None):
        return _not_implemented()

## ONNX Region ##

class ONNXHelper(IHelper):

    def _clean_initializers(self, model, verbose = False):
        inits = [e.name for e in model.graph.initializer]
        index = len(model.graph.input)
        for obj in model.graph.input[::-1]:
            index -= 1
            if obj.name in inits:
                _ = model.graph.input.pop(index)
                if verbose:
                    print("Remove initializer {} from graph input".format(obj.name))

    def __init__(self, filepath):
        super().__init__(filepath=filepath)
        import onnx
        self._model_proto = onnx.load(filepath)
        self._clean_initializers(self._model_proto)

    def show_discription(self):
        if self._model_proto.producer_name:
            if self._model_proto.producer_version:
                print("Producer: {}, version: {}".format(self._model_proto.producer_name, self._model_proto.producer_version))
            else:
                print("Producer: {}".format(self._model_proto.producer_name))
        if self._model_proto.opset_import:
            print("Opset import:", self._model_proto.opset_import)
        if self._model_proto.ir_version:
            print("IR version:", self._model_proto.ir_version)

    def show_nodes(self):
        print(self._model_proto.graph.node)
        print("Total number of node:", len(self._model_proto.graph.node))

    def show_inputs(self):
        print(self._model_proto.graph.input)
        print("Total number of input:", len(self._model_proto.graph.input))

    def show_outputs(self):
        print(self._model_proto.graph.output)
        print("Total number of output:", len(self._model_proto.graph.output))

    def to_external_data(self, filepath = None, location = None):
        from onnx.external_data_helper import convert_model_to_external_data
        f = filepath if filepath else self._filepath.replace(".onnx", "_ext.onnx")
        loc = location if location else os.path.basename(self._filepath).replace(".onnx", "_ext.bin")
        convert_model_to_external_data(self._model_proto, all_tensors_to_one_file=True, location=loc)
        onnx.save(self._model_proto, f)

## Tensorflow Region ##

def _load_tf_graphdef(model_path):
    """Load tensorflow graph from graphdef."""
    from google.protobuf.message import DecodeError
    from tensorflow.core.protobuf import saved_model_pb2
    from tensorflow.python.util import compat
    # make sure we start with clean default graph
    tf1.reset_default_graph()
    with tf1.Session() as sess:
        graph_def = tf1.GraphDef()
        with tf1.gfile.GFile(model_path, 'rb') as f:
            try:
                content = f.read()
            except Exception as e:
                raise OSError(
                    "Unable to load file '{}'.".format(model_path)) from e
            try:
                graph_def.ParseFromString(content)
            except DecodeError:
                content_as_bytes = compat.as_bytes(content)
                saved_model = saved_model_pb2.SavedModel()
                saved_model.ParseFromString(content_as_bytes)
                graph_def = saved_model.meta_graphs[0].graph_def
            except Exception as e:
                raise RuntimeError(
                    "Unable to parse file '{}'.".format(model_path)) from e
    return graph_def

def _load_tf_checkpoint(model_path):
    """Load tensorflow graph from checkpoint."""
    # make sure we start with clean default graph
    tf1.reset_default_graph()
    # model_path = checkpoint/checkpoint.meta
    with tf1.device("/cpu:0"):
        with tf1.Session() as sess:
            saver = tf1.train.import_meta_graph(model_path, clear_devices=True)
            # restore from model_path minus the ".meta"
            saver.restore(sess, model_path[:-5])
            return sess.graph_def

def _load_tf_keras_h5(model_path):
    """Load keras model - experimental for now."""
    from tensorflow.python import keras as _keras
    #from tensorflow.python.eager import context
    #from tensorflow.python.keras.saving import saving_utils as _saving_utils
    # Handles Keras when Eager mode is enabled.
    custom_objects = {'tf': tf}
    with tf1.device("/cpu:0"):
        _keras.backend.clear_session()
        _keras.backend.set_learning_phase(False)
        _ = _keras.models.load_model(model_path, custom_objects)
        sess = _keras.backend.get_session()
        return sess.graph_def

def _show_tf_graphdef_discription(graph_def):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
    # TODO: @someone
    print("Tensorflow graphdef: ...")

def _show_tf_graphdef_nodes(graph_def):
    for i, n in enumerate(graph_def.node):
        # <class 'tensorflow.core.framework.node_def_pb2.NodeDef'>
        # other members: attr, device, input, etc.
        print("Node[%d]: %s, %s" % (i, n.name, n.op))
    print("Total number of node:", len(graph_def.node))

def _show_tf_graphdef_inputs(graph_def):
    inputs = []
    for i, n in enumerate(graph_def.node):
        # <class 'tensorflow.core.framework.node_def_pb2.NodeDef'>
        # other members: attr, device, input, etc.
        if n.op == "Placeholder":
            print("Input[%d]: %s" % (i, n.name))
            print("attr:", n.attr)
            inputs.append(n)
    print("Total number of input:", len(inputs))

def _show_tf_graphdef_outputs(graph_def):
    node_list = [n.name for n in graph_def.node]
    node_used = [i.split(':')[0] for n in graph_def.node for i in n.input]
    # TODO: maybe some optimizations are neede(e.g. eliminate useless tensor)
    outputs = [":".join([o, '0']) for o in node_list if o not in node_used and "^"+o not in node_used]
    for i, o in enumerate(outputs):
        print("Output[%d]: %s" % (i, o))
    print("Total number of output:", len(outputs))


class TFHelper(IHelper):

    def __init__(self, filepath):
        super().__init__(filepath=filepath)
        self._show_discription = _not_implemented
        self._show_nodes = _not_implemented
        self._show_inputs = _not_implemented
        self._show_outputs = _not_implemented
        self._to_external_data = _not_implemented
        suffix = os.path.splitext(filepath)[-1]
        if suffix in [".pb", ".meta", ".h5"]:
            if suffix == ".pb":
                self._graphdef = _load_tf_graphdef(filepath)
            elif suffix == ".meta":
                self._graphdef = _load_tf_checkpoint(filepath)
            else: # ".h5"
                self._graphdef = _load_tf_keras_h5(filepath)
            self._show_discription = lambda: _show_tf_graphdef_discription(self._graphdef)
            self._show_nodes = lambda: _show_tf_graphdef_nodes(self._graphdef)
            self._show_inputs = lambda: _show_tf_graphdef_inputs(self._graphdef)
            self._show_outputs = lambda: _show_tf_graphdef_outputs(self._graphdef)
            #self._to_external_data = _not_implemented
        else:
            raise NotImplementedError("Sorry, not supported to load {} yet.".fromat(filepath))

    def show_discription(self):
        return self._show_discription()

    def show_nodes(self):
        return self._show_nodes()

    def show_inputs(self):
        return self._show_inputs()

    def show_outputs(self):
        return self._show_outputs()

    def to_external_data(self, filepath=None, location=None):
        return self._to_external_data(filepath, location)


def get_argsparser_detail(parser = None, epilog = None):
    if parser is None:
        parser = argparse.ArgumentParser(description="{} model(s) helper.".format("JDSK"),
                                         formatter_class=argparse.RawDescriptionHelpFormatter, epilog=_HELP_TEXT)
    parser.add_argument('--onnx', type=str, default=None, help="The input onnx model path.")
    parser.add_argument('--graphdef', type=str, default=None, help="The input tensorflow protobuf model path.")
    parser.add_argument('--checkpoint', type=str, default=None, help="The input tensorflow checkpoint meta path.")
    parser.add_argument('--keras', type=str, default=None, help="The input tensorflow keras h5 filepath.")
    parser.add_argument('--show_node', '-sn', action='store_true', default=False, help="Display model graph nodes.")
    parser.add_argument('--show_input', '-si', action='store_true', default=False, help="Display model graph inputs.")
    parser.add_argument('--show_output', '-so', action='store_true', default=False, help="Display model graph outputs.")
    parser.add_argument('--to_ext_data', '-ext', action='store_true', default=False, help="Convert model to external data(ONNX only).")
    parser.add_argument("--verbose", "-v", default=0, help="verbose output, option is additive", action="count")
    return parser


def show_detail(args):
    if not (args.onnx or args.graphdef or args.checkpoint or args.keras):
        # TODO: How to call parser.print_help()?
        parser = get_argsparser_detail(epilog=_HELP_TEXT)
        parser.print_usage() # print_help()
        return 1

    helper = None
    if not helper and args.onnx:
        global onnx
        import onnx
        helper = ONNXHelper(args.onnx)
    if not helper and (args.graphdef or args.checkpoint or args.keras):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        global tf1
        try:
            import tensorflow.compat.v1 as tf1
            tf1.disable_v2_behavior()
        except ImportError:
            import tensorflow as tf1
        if args.graphdef:
            helper = TFHelper(args.graphdef)
        elif args.checkpoint:
            helper = TFHelper(args.checkpoint)
        elif args.keras:
            helper = TFHelper(args.keras)
        else:
            pass
    if args.verbose:
        helper.show_discription()
    if args.show_node:
        helper.show_nodes()
    if args.show_input:
        helper.show_inputs()
    if args.show_output:
        helper.show_outputs()
    if args.to_ext_data:
        helper.to_external_data()
    return 0


def main():
    parser = get_argsparser_detail(epilog=_HELP_TEXT)
    args = parser.parse_args()
    if not (args.onnx or args.graphdef or args.checkpoint or args.keras):
        parser.print_help()
        sys.exit(1)
    return(show_detail(args))


if __name__ == "__main__":
    import sys
    if sys.argv[-1] == '#%s' % magic:
        del sys.argv[-1]
    sys.exit(main())


del magic
