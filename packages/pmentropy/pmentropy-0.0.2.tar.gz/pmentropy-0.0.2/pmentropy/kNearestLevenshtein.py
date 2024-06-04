import numpy as np
from tools import minimum
import multiprocessing
from Levenshtein import distance

def get_prefixes(key: str) -> list:
    return key.split("/")

def levenshtein(s: list, t: list):
    m = len(s)
    n = len(t)
    shortest = min(m, n)

    # skip matching prefixes
    k = 0
    while s[k] == t[k]:
        if k == shortest - 1:
            break
        k += 1
    
    # skip matching suffixes
    l = 0
    while s[m - l - 1] == t[n - l - 1]:
        l += 1
        if shortest - l - k <= 0:
            break
    
    shrt = s[k:(m - l)]
    lng = t[k:(n - l)]
    if len(shrt) > len(lng):
        shrt = t
        lng = s
    m = len(shrt)
    n = len(lng)

    buffer = [0] * (m + 1)
    for i in range(m + 1):
        buffer[i] = i
    for i in range(1, n + 1):
        tmp = buffer[0]
        buffer[0] += 1

        for j in range(1, len(buffer)):
            p = buffer[j - 1]
            r = buffer[j]
            eql = 1 if 0 == len(shrt) or 0 == len(lng) or lng[i - 1] != shrt[j - 1] else 0
            tmp = min(p + 1, r + 1, tmp + eql)
            tmp, buffer[j] = buffer[j], tmp
    
    return buffer[m]

def levenshteinNormalize(s: list, t: list):
    #return levenshtein(s, t) / max(len(s), len(t))
    return distance(s, t) / max(len(s), len(t))


def next_i(args):
    i, end_nodes_path, s, n = args
    res = [0] * (n - i)
    for j in range(i, n):
            if i == j:
                res[j - i] = float("inf")
                continue
            t = get_prefixes(end_nodes_path[j])

            d = levenshteinNormalize(s, t)
            res[j - i] = d
    return res

def kNearestLevenshtein(k: int, normalize: bool, end_node: list) -> list:
    result = []
    n = len(end_node)
    distanceMatrix = np.zeros((n, n))
    pool = multiprocessing.Pool()

    end_node_path = list(map(lambda x: x.path, end_node))
    args = [(i, end_node_path, get_prefixes(end_node_path[i]), n) for i in range(n)]
    vals_i = pool.map(next_i, args)
    for i in range(n):
        for jp, d in enumerate(vals_i[i]):
            j = jp + i
            distanceMatrix[i, j] = d
            distanceMatrix[j, i] = d

    k = min(k, n)
    for i in range(n):
        result.append(minimum(distanceMatrix[i], k))
        
    return result

