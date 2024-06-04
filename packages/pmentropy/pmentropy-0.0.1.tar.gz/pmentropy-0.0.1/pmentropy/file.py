from pm4py.streaming.importer.xes import importer as xes_importer
from pmentropy.tools import add_mapping_key, increment_trie, increment_end_trie
from pmentropy.Node import Node

def read_file(file_path: str, flatten=False) -> tuple[dict[Node], dict]:
    """
    This function parse logs from a xes file.

    :param file_path: this is a file path
    :param flatten: generate flatten trie
    :return: couple of the trie and informations about the trie
    """
    stream = xes_importer.apply(file_path, variant=xes_importer.xes_trace_stream)
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

    if flatten:
        for trace in stream:
            keys = []
            for event in trace:
                keys.append(add_mapping_key(mapping, event["concept:name"]))
            
            key_test = "/".join(keys)
            if key_test not in trie or not trie[key_test].is_end_node():
                if len(keys) > trie_infos["longest_branch"]:
                    trie_infos["longest_branch"] = len(keys)
                increment_event(keys)
    else:
        for trace in stream:
            keys = []
            for event in trace:
                keys.append(add_mapping_key(mapping, event["concept:name"]))

            if len(keys) > trie_infos["longest_branch"]:
                trie_infos["longest_branch"] = len(keys)
            increment_event(keys)

    return trie, trie_infos
