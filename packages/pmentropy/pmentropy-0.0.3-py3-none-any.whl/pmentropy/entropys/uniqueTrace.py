from pmentropy.Node import Node

def unique_trace(logs: tuple[dict[Node], dict]):
    trie, trie_infos = logs
    total_traces = 0
    unique_traces = 0

    for node in trie_infos["end_nodes"]:
        total_traces += node.get_end_visits()
        unique_traces += 1
    return unique_traces / total_traces