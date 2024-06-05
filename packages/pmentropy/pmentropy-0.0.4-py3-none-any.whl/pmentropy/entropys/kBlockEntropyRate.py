from .kBlockEntropy import k_block_entropy
from pmentropy.Node import Node
import math

def get_rate_ratio(H_k: float, H_k_minus1: float, k: int):
    return H_k / k

def get_rate_diff(H_k: float, H_k_minus1: float, k: int):
    return H_k - H_k_minus1

tests = {
    1: lambda h, k, K, S: k > math.log2(K) / h,
    2: lambda h, k, K, S: k > K * h / math.log2(S),
    3: lambda h, k, K, S: k * pow(S, k) > K,
    4: lambda h, k, K, S: K * h < k * pow(S, k) * math.log2(S),
    5: lambda h, k, K, S: K * h < k * pow(2, k * h) * math.log2(S),
}
def k_block_entropy_rate_ratio(logs: tuple[dict[Node], dict], c: int):
    return kBlockEntropyRate("ratio", logs, c)

def k_block_entropy_rate_diff(logs: tuple[dict[Node], dict], c: int):
    return kBlockEntropyRate("diff", logs, c)

def kBlockEntropyRate(type: str, logs: tuple[dict[Node], dict], c: int):
    trie, trie_infos = logs
    K = trie_infos["longest_branch"]
    k_block_map = {}
    S = len(trie_infos["mapping"])
    H_k_minus1 = 0.0
    result = None
    last_result = None
    k_cut_of  = 0

    for k in range(1, K + 1):
        H_k = k_block_map.get(k)
        if H_k is None:
            H_k = k_block_entropy(logs, k)
            k_block_map[k] = H_k

        h_k = get_rate_ratio(H_k, H_k_minus1, k) if type == "ratio" else get_rate_diff(H_k, H_k_minus1, k)
        H_k_minus1 = H_k
        last_result = result
        result = h_k
        k_cut_of = k

        if tests[c](h_k, k, K, S):
            break

    return (last_result, k_cut_of - 1) if type == "ratio" and last_result is not None else (result, k_cut_of)