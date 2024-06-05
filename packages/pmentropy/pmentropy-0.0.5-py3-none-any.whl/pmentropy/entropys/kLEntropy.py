import numpy as np
import math
from pmentropy.kNearestLevenshtein import kNearestLevenshtein
from pmentropy.Node import Node

def kL_entropy(logs: tuple[dict[Node], dict], p: int) -> float:
    """
    Compute the KL entropy
    """
    trie, trie_infos = logs
    end_nodes = trie_infos["end_nodes"]
    if len(end_nodes) < 2:
        raise "Not enough activities to compute the entropy"
    
    acc = 0.0
    distances_set = kNearestLevenshtein(1, True, end_nodes)
    n = len(distances_set)

    V = pow(math.pi, p / 2.0) / math.gamma(p / 2.0 + 1)
    for distances in distances_set:
        d = distances[0]
        acc += math.log(d) + math.log(V) + np.euler_gamma + math.log(n - 1)
    
    return acc * p / n