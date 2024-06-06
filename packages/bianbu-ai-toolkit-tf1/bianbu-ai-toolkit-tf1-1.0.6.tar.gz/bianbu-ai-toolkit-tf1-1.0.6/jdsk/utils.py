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
# 2023/09/24  v0.0.2  support onnx model with input tensor type 'sequence_type'
# 2023/08/30  v0.0.1  init commit

import onnx
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


def clean_initializers(model, verbose = False):
    inits = [e.name for e in model.graph.initializer]
    index = len(model.graph.input)
    for obj in model.graph.input[::-1]:
        index -= 1
        if obj.name in inits:
            _ = model.graph.input.pop(index)
            if verbose:
                print("Remove initializer {} from graph input".format(obj.name))


def get_input_output_names(model):
    input_names = [e.name for e in model.graph.input]
    output_names = [e.name for e in model.graph.output]
    return input_names, output_names

"""
def get_input_output_shape(model):
    input_shape  = [[d.dim_value for d in e.type.tensor_type.shape.dim] for e in model.graph.input]
    output_shape = [[d.dim_value for d in e.type.tensor_type.shape.dim] for e in model.graph.output]
    return input_shape, output_shape

def get_input_output_dtype(model):
    input_dtype  = [ONNX_DTYPE_NAMES[e.type.tensor_type.elem_type] for e in model.graph.input]
    output_dtype = [ONNX_DTYPE_NAMES[e.type.tensor_type.elem_type] for e in model.graph.output]
    return input_dtype, output_dtype
"""

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


def get_input_value_info(model):
    type_info = [(_get_type_proto_info(vi.type)) for vi in model.graph.input]
    return [vi.name for vi in model.graph.input], [e[0] for e in type_info], [e[1] for e in type_info]


def get_output_value_info(model):
    type_info = [(_get_type_proto_info(vi.type)) for vi in model.graph.output]
    return [vi.name for vi in model.graph.output], [e[0] for e in type_info], [e[1] for e in type_info]


def split_nodename_and_shape(name): # type: (str) -> (List[str], Dict[str, List[int]])
    """
        This function is similar to tf2onnx.utils.split_nodename_and_shape, which split input name with shape
        into name and shape. What's more, it also supports input name with dynamic shape, i.e. str parameters,
        e.g. input_1:0[unk,3,224,224].
    """
    import re
    # pattern for a node name
    inputs = []
    shapes = {}
    # input takes in most cases the format name:0, where 0 is the output number
    # in some cases placeholders don't have a rank which onnx can't handle so we let uses override the shape
    # by appending the same, ie : [1,28,28,3]
    name_pattern = re.compile(r"(?:([\w\d/\-\._:]+)(\[[\w\_\-\d,]+\])?),?")
    splits = re.split(name_pattern, name)
    for i in range(1, len(splits), 3):
        inputs.append(splits[i])
        if splits[i + 1] is not None:
            shape = [int(n) if n.isdigit() else n for n in splits[i + 1][1:-1].split(",")]
            shapes[splits[i]] = shape
    return inputs, shapes if shapes else None


def override_free_dimensions(model, dim_params = {}, denotations = {}): # type: (ModelProto, Dict[str, int], Dict[str, int]) -> ModelProto

    def update_dim_proto(dim_proto, value = None, param = None, denotation = None):
        # check class type first
        #assert(isinstance(dim_proto, onnx.onnx_ml_pb2.Dimension))
        # we also support to update free dimension param name and denotation
        if isinstance(value, int):
            dim_proto.dim_value = value
        else:
            if isinstance(param, str):
                if param.isdecimal():
                    dim_proto.dim_value = int(param)
                else:
                    dim_proto.dim_param = param
            if isinstance(denotation, str):
                if denotation.isdecimal():
                    dim_proto.dim_value = int(denotation)
                else:
                    dim_proto.denotation = denotation
        return dim_proto

    def update_tensor_type(value_infos, dim_param_dict, denotation_dict):
        _dim_params, _denotations = dim_param_dict.keys(), denotation_dict.keys()
        # walk through all value info object and override matched free dimensions
        for vi in value_infos:
            for i, dim_proto in enumerate(vi.type.tensor_type.shape.dim):
                if dim_proto.HasField("dim_value"):
                    pass
                else:
                    bingo_param = dim_proto.HasField("dim_param") and dim_proto.dim_param in _dim_params
                    bingo_denotation = dim_proto.HasField("denotation") and dim_proto.denotation in _denotations
                    if bingo_param and bingo_denotation and dim_param_dict[dim_proto.dim_param] != denotation_dict[dim_proto.denotation]:
                        raise ValueError(
                            "{} shape[{}] matches both dim_param(\"{}\") and denotation(\"{}\"), while input override value incompatible {} vs {}".format(
                                vi.name, i, dim_proto.dim_param, dim_proto.denotation, dim_param_dict[dim_proto.dim_param], denotation_dict[dim_proto.denotation])
                        )
                    if bingo_param:
                        _ = update_dim_proto(dim_proto, value=None, param=dim_param_dict[dim_proto.dim_param], denotation=None)
                    if bingo_denotation:
                        _ = update_dim_proto(dim_proto, value=None, param=None, denotation=denotation_dict[dim_proto.denotation])

    if len(dim_params) or len(denotations):
        update_tensor_type(model.graph.input, dim_params, denotations)
        update_tensor_type(model.graph.output, dim_params, denotations)
        onnx.checker.check_model(model)

    return model


def update_inputs_outputs_dims(model, input_dims, output_dims): # type: (ModelProto, Dict[str, List[Any]], Dict[str, List[Any]]) -> ModelProto
    """
        This function is similar to onnx.tools.update_model_dims.update_inputs_outputs_dims. It updates the
        dimension sizes of the model's inputs and outputs to the values provided in input_dims and output_dims.
        If the dim value provided is negative, a unique dim_param will be set for that dimension. What's more,
        if the value info of model's inputs and outputs missing the shape dimension size info, this function
        can also fix or update it with the values provided in input_dims and output_dims.
    """
    dim_param_set = set()  # type: Set[str]

    def init_dim_param_set(dim_param_set, value_infos):  # type: (Set[str], List[ValueInfoProto]) -> None
        for info in value_infos:
            shape = info.type.tensor_type.shape
            for dim in shape.dim:
                if dim.HasField("dim_param"):
                    dim_param_set.add(dim.dim_param)  # type: ignore

    init_dim_param_set(dim_param_set, model.graph.input)  # type: ignore
    init_dim_param_set(dim_param_set, model.graph.output)  # type: ignore
    init_dim_param_set(dim_param_set, model.graph.value_info)  # type: ignore

    def update_dim(tensor, dim, j, name):  # type: (ValueInfoProto, Any, int, str) -> None
        dim_proto = tensor.type.tensor_type.shape.dim[j]
        if isinstance(dim, int):
            if dim >= 0:
                if dim_proto.HasField("dim_value") and dim_proto.dim_value != dim:
                    raise ValueError(
                        "Unable to set dimension value to {} for axis {} of {}. Contradicts existing dimension value {}.".format(
                            dim, j, name, dim_proto.dim_value
                        )
                    )
                dim_proto.dim_value = dim
            else:
                generated_dim_param = name + "_" + str(j)
                if generated_dim_param in dim_param_set:
                    raise ValueError(
                        "Unable to generate unique dim_param for axis {} of {}. Please manually provide a dim_param value.".format(
                            j, name
                        )
                    )
                dim_proto.dim_param = generated_dim_param
        elif isinstance(dim, str):
            dim_proto.dim_param = dim
        else:
            raise ValueError(
                f"Only int or str is accepted as dimension value, incorrect type: {type(dim)}"
            )

    def update_tensor_type(value_infos, shape_dict):
        update_names = shape_dict.keys()
        for vi in value_infos:
            vi_name = vi.name
            if vi_name in update_names:
                update_dim_arr = shape_dict[vi_name]
                update_dim_len, vi_dim_len = len(update_dim_arr), len(vi.type.tensor_type.shape.dim)
                if vi_dim_len and vi_dim_len != update_dim_len:
                    raise ValueError(
                        "Update shape dim not match {} vs {}".format(vi.type.tensor_type.shape.dim, update_dim_arr)
                    )
                elif vi_dim_len == 0:
                    # value info missing shape dim
                    tensor_type = onnx.helper.make_tensor_type_proto(vi.type.tensor_type.elem_type, update_dim_arr)
                    vi.type.CopyFrom(tensor_type)
                else:
                    # vi_dim_len equal to update_dim_len
                    for j, dim in enumerate(update_dim_arr):
                        update_dim(vi, dim, j, vi_name)

    if input_dims:
        update_tensor_type(model.graph.input, input_dims)
    if output_dims:
        update_tensor_type(model.graph.output, output_dims)

    #onnx.checker.check_model(model)
    return model


__all__ = [
    "get_input_output_names",
    #"get_input_output_shape",
    #"get_input_output_dtype",
    "get_input_value_info",
    "get_output_value_info"
    "split_nodename_and_shape",
    "update_inputs_outputs_dims",
    "override_free_dimensions",
]
