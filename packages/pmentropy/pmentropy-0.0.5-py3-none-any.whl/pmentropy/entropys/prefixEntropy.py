import math
from pmentropy.Node import Node
from pmentropy.tools import for_key_in_trie

def prefix_entropy(logs: tuple[dict[Node], dict]) -> float:
    """
    Compute the prefix entropy
    """
    trie, trie_infos = logs
    total = 0
    for key in for_key_in_trie(trie):
        total += trie[key].get_visits()
    acc = 0.0
    for key in for_key_in_trie(trie):
        value = trie[key].get_visits()
        if value == 0:
            continue
        p = value / total
        acc -= p * math.log2(p)
    return acc


    