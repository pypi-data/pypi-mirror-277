import flatbuffers

from typing import List, Dict
from generated import (
    InputSeries,
    DataKVP,
    ValueGraph,
    NodeKVP,
    Node,
    Parameter,
    LogicGraph,
    IndicatorRequest,
    FBArray,
)


def serialize_arr(arr: List[float]):
    builder = flatbuffers.Builder(1024)

    FBArray.StartVVector(builder, len(arr))
    for value in reversed(arr):
        builder.PrependFloat32(value)
    fbb_values = builder.EndVector(len(arr))

    FBArray.ArrStart(builder)
    FBArray.AddV(builder, fbb_values)
    fbb_arr = FBArray.ArrEnd(builder)

    builder.Finish(fbb_arr)

    return builder.Output()


def serialize_indicator_request(
    name: str, _data: Dict[str, float], parameters: Dict[str, str]
):
    builder = flatbuffers.Builder(1024)

    fbb_name = builder.CreateString(name)

    data = []

    for k, v in _data.items():
        fbb_key = builder.CreateString(k)

        values = []

        for _v in v:
            values.append(_v)

        DataKVP.DataKVPStartValueVector(builder, len(values))
        for _v in reversed(values):
            builder.PrependFloat32(_v)
        fbb_value = builder.EndVector(len(values))

        DataKVP.DataKVPStart(builder)
        DataKVP.AddKey(builder, fbb_key)
        DataKVP.AddValue(builder, fbb_value)
        data.append(DataKVP.DataKVPEnd(builder))

    IndicatorRequest.StartDataVector(builder, len(data))
    for fbb_value in reversed(data):
        builder.PrependUOffsetTRelative(fbb_value)
    fbb_data = builder.EndVector(len(data))

    params = []

    for k, v in parameters.items():
        fbb_key = builder.CreateString(k)
        fbb_value = builder.CreateString(v)

        Parameter.ParameterStart(builder)
        Parameter.AddKey(builder, fbb_key)
        Parameter.AddValue(builder, fbb_value)
        params.append(Parameter.ParameterEnd(builder))

    IndicatorRequest.StartParametersVector(builder, len(params))
    for fbb_param in reversed(params):
        builder.PrependUOffsetTRelative(fbb_param)
    fbb_parameters = builder.EndVector(len(params))

    IndicatorRequest.IndicatorRequestStart(builder)

    IndicatorRequest.AddName(builder, fbb_name)
    IndicatorRequest.AddData(builder, fbb_data)
    IndicatorRequest.AddParameters(builder, fbb_parameters)

    fbb_indicator = IndicatorRequest.IndicatorRequestEnd(builder)

    builder.Finish(fbb_indicator)

    return builder.Output()


def serialize_node(builder: flatbuffers.Builder, dict_node: Dict[str, str]):
    fbb_type = builder.CreateString(dict_node["type"])
    fbb_name = builder.CreateString(dict_node["name"])

    fbb_parameters = []

    if "parameters" in dict_node:
        for k, v in dict_node["parameters"].items():
            fbb_key = builder.CreateString(k)
            fbb_value = builder.CreateString(v)

            Parameter.ParameterStart(builder)
            Parameter.AddKey(builder, fbb_key)
            Parameter.AddValue(builder, fbb_value)
            fbb_parameters.append(Parameter.ParameterEnd(builder))

    Node.StartParametersVector(builder, len(fbb_parameters))
    for fbb_param in reversed(fbb_parameters):
        builder.PrependUOffsetTRelative(fbb_param)
    fbb_parameters = builder.EndVector(len(fbb_parameters))

    fbb_parents = []

    if "parents" in dict_node:
        for p in dict_node["parents"]:
            fbb_parents.append(builder.CreateString(p))

    Node.StartParentsVector(builder, len(fbb_parents))
    for fbb_parent in reversed(fbb_parents):
        builder.PrependUOffsetTRelative(fbb_parent)
    fbb_parents = builder.EndVector(len(fbb_parents))

    fbb_true_child = None
    if "true_child" in dict_node:
        fbb_true_child = builder.CreateString(dict_node["true_child"])

    fbb_false_child = None
    if "false_child" in dict_node:
        fbb_false_child = builder.CreateString(dict_node["false_child"])

    Node.NodeStart(builder)

    Node.AddType(builder, fbb_type)
    Node.AddName(builder, fbb_name)
    Node.AddParameters(builder, fbb_parameters)
    Node.AddParents(builder, fbb_parents)

    if fbb_true_child:
        Node.AddTrueChild(builder, fbb_true_child)

    if fbb_false_child:
        Node.AddFalseChild(builder, fbb_false_child)

    return Node.NodeEnd(builder)


def serialize_value_graph(nodes: Dict[str, Dict[str, str]], leaves: List[str]):
    builder = flatbuffers.Builder(1024)

    fbb_node_kvps = []

    for k, v in nodes.items():
        fbb_key = builder.CreateString(k)
        fbb_node = serialize_node(builder, v)

        NodeKVP.NodeKVPStart(builder)
        NodeKVP.AddKey(builder, fbb_key)
        NodeKVP.AddValue(builder, fbb_node)
        fbb_node_kvps.append(NodeKVP.NodeKVPEnd(builder))

    ValueGraph.StartNodesVector(builder, len(fbb_node_kvps))
    for fbb_node in reversed(fbb_node_kvps):
        builder.PrependUOffsetTRelative(fbb_node)
    fbb_nodes = builder.EndVector(len(fbb_node_kvps))

    fbb_leaf_strs = []

    for leaf in leaves:
        fbb_leaf_strs.append(builder.CreateString(leaf))

    ValueGraph.StartLeavesVector(builder, len(fbb_leaf_strs))
    for fbb_leaf in reversed(fbb_leaf_strs):
        builder.PrependUOffsetTRelative(fbb_leaf)
    fbb_leaves = builder.EndVector(len(fbb_leaf_strs))

    ValueGraph.ValueGraphStart(builder)
    ValueGraph.AddLeaves(builder, fbb_leaves)
    ValueGraph.AddNodes(builder, fbb_nodes)

    fbb_value_graph = ValueGraph.ValueGraphEnd(builder)

    builder.Finish(fbb_value_graph)

    return builder.Output()


def serialize_logic_graph(nodes: Dict[str, Dict[str, str]], root: str):
    builder = flatbuffers.Builder(1024)

    fbb_node_kvps = []

    for k, v in nodes.items():
        fbb_key = builder.CreateString(k)
        fbb_node = serialize_node(builder, v)

        NodeKVP.NodeKVPStart(builder)
        NodeKVP.AddKey(builder, fbb_key)
        NodeKVP.AddValue(builder, fbb_node)
        fbb_node_kvps.append(NodeKVP.NodeKVPEnd(builder))

    LogicGraph.StartNodesVector(builder, len(fbb_node_kvps))
    for fbb_node in reversed(fbb_node_kvps):
        builder.PrependUOffsetTRelative(fbb_node)
    fbb_nodes = builder.EndVector(len(fbb_node_kvps))

    fbb_root = builder.CreateString(root)

    LogicGraph.LogicGraphStart(builder)
    LogicGraph.AddRoot(builder, fbb_root)
    LogicGraph.AddNodes(builder, fbb_nodes)

    fbb_logic_graph = LogicGraph.LogicGraphEnd(builder)

    builder.Finish(fbb_logic_graph)

    return builder.Output()


def serialize_input_series(
    _type: str, c0: float, dates: List[str], data: Dict[str, List[float]]
):
    builder = flatbuffers.Builder(1024)

    fbb_type = builder.CreateString(_type)

    fbb_date_strs = []

    for date in dates:
        fbb_date_strs.append(builder.CreateString(date))

    InputSeries.StartDatesVector(builder, len(fbb_date_strs))
    for fbb_date in reversed(fbb_date_strs):
        builder.PrependUOffsetTRelative(fbb_date)
    fbb_dates = builder.EndVector(len(fbb_date_strs))

    fbb_data_kvps = []

    for k, v in data.items():
        fbb_key = builder.CreateString(k)

        DataKVP.StartValuesVector(builder, len(v))
        for value in reversed(v):
            builder.PrependFloat32(value)
        fbb_values = builder.EndVector(len(v))

        DataKVP.DataKVPStart(builder)
        DataKVP.AddKey(builder, fbb_key)
        DataKVP.AddValues(builder, fbb_values)
        fbb_data_kvps.append(DataKVP.DataKVPEnd(builder))

    InputSeries.StartDataVector(builder, len(data))
    for data_kvp in fbb_data_kvps:
        builder.PrependUOffsetTRelative(data_kvp)
    fbb_data = builder.EndVector(len(fbb_data_kvps))

    InputSeries.InputSeriesStart(builder)
    InputSeries.AddType(builder, fbb_type)
    InputSeries.AddC0(builder, c0)
    InputSeries.AddDates(builder, fbb_dates)
    InputSeries.AddData(builder, fbb_data)

    fbb_input_series = InputSeries.InputSeriesEnd(builder)

    builder.Finish(fbb_input_series)

    return builder.Output()
