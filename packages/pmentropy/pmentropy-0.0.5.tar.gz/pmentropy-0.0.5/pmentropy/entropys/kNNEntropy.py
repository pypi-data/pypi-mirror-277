from pmentropy.Node import Node
from pmentropy.kNearestLevenshtein import kNearestLevenshtein
import math
import numpy as np

def L(j: int) -> float:
    if j < 0:
        return None
    if j == 0:
        return 0.0
    L_j = 0.0
    for i in range(1, j + 1):
        L_j += 1.0 / i
    return L_j

def kNN_entropy(logs: tuple[dict[Node], dict], k: int, p: int) -> float:
    """
    Compute the kNN entropy
    """
    trie, trie_infos = logs
    end_nodes = trie_infos["end_nodes"]

    distances_set = kNearestLevenshtein(k, True, end_nodes)
    
    acc = 0.0
    n = len(distances_set)
    V = pow(math.pi, p / 2.0) / math.gamma(p / 2.0 + 1)
    for distances in distances_set:
        d = max(distances)
        acc += math.log(d) + math.log(V) + np.euler_gamma - L(k - 1) + math.log(n)
    return acc * p / n