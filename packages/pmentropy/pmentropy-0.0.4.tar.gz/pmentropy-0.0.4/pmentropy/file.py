from pm4py.streaming.importer.xes import importer as xes_importer
from pandas import DataFrame
from typing import Callable
from .tools import add_mapping_key, increment_trie, increment_end_trie
from .Node import Node

def read_file(file_path: str, flatten=False) -> tuple[dict[Node], dict]:
    """
    This function parse logs from a xes file.

    :param file_path: this is a file path
    :param flatten: generate flatten trie
    :return: couple of the trie and informations about the trie
    """
    stream = xes_importer.apply(file_path, variant=xes_importer.xes_trace_stream)
    next_trace, res = read_trace_by_trace(flatten)
    for trace in stream:
        next_trace(trace)

    return res

def read_trace_by_trace(flatten=False) -> tuple[Callable, tuple[dict[Node], dict]]:
    """
    This function parse logs with a trace by trace approach.

    :param flatten: generate flatten trie
    """
    trie = {}
    mapping = {}
    trie_infos = {
        "longest_branch": 0,
        "mapping": mapping,
        "end_nodes": []
    }

    def increment_event(keys):
        total_key = keys[0]
        parent = increment_trie(trie, total_key)
        for i in range(1, len(keys)):
            total_key += "/" + keys[i]
            parent = increment_trie(trie, total_key, parent)

        increment_end_trie(trie, trie_infos, total_key, parent)


    def next_trace_flatten(trace):
        keys = []
        for event in trace:
            keys.append(add_mapping_key(mapping, event["concept:name"]))
        
        key_test = "/".join(keys)
        if key_test not in trie or not trie[key_test].is_end_node():
            if len(keys) > trie_infos["longest_branch"]:
                trie_infos["longest_branch"] = len(keys)
            increment_event(keys)
    
    def next_trace(trace):
        keys = []
        for event in trace:
            keys.append(add_mapping_key(mapping, event["concept:name"]))

        if len(keys) > trie_infos["longest_branch"]:
            trie_infos["longest_branch"] = len(keys)
        increment_event(keys)
        
    return next_trace_flatten if flatten else next_trace, (trie, trie_infos)


def read_DataFrame(logs: DataFrame, flatten=False) -> tuple[dict[Node], dict]:
    """
    This function parse logs from datafrom of logs.

    :param logs: the dataframe
    :param flatten: generate flatten trie
    :return: couple of the trie and informations about the trie
    """
    next_trace, res = read_trace_by_trace(flatten)
    events_of_trace = []
    current_trace_name = None

    for ind in logs.index:
        trace_name = logs.loc[ind, "case:concept:name"]
        if current_trace_name != trace_name:
            if current_trace_name is not None:
                next_trace(events_of_trace)
            current_trace_name = trace_name
            events_of_trace = []
        events_of_trace.append(logs.loc[ind])

    return res