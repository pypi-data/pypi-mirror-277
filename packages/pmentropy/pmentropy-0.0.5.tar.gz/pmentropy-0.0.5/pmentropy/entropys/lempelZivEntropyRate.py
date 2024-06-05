from pmentropy.Node import Node
import math

def lempel_ziv_entropy_rate(logs: tuple[dict[Node], dict]):
    """
    Compute the Lempel-Ziv entropy rate
    """
    trie, trie_infos = logs
    words = []
    N = 0
    for node in trie_infos["end_nodes"]:
        word = []
        trace_list = node.path.split("/")

        for activity in trace_list:
            word.append(activity)
            if word not in words:
                words.append(word)
                word = []
        N += len(trace_list) * node.get_end_visits()
            
    N_w = len(words)
    return math.log2(N) * N_w / N