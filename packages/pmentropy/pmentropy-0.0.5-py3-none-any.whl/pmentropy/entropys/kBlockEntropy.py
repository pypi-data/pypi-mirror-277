from pmentropy.tools import for_key_in_trie
from pmentropy.Node import Node
import math

def k_block_entropy(logs: tuple[dict[Node], dict], k: int) -> float:
    """
    Compute the k block entropy
    """
    trie, trie_infos = logs
    acc = 0.0
    total_block_count = 0
    n_gram_trie = {}

    for key in for_key_in_trie(trie):
        depth = key.count("/") + 1
        if depth < k:
            continue
        current_end_node = trie[key]

        for _ in range(depth, k-1, -1):
            block = []
            current_node = current_end_node
            for _ in range(k, 0, -1):
                element = current_node.key
                block.append(element)
                current_node = current_node.parent
            block.reverse()
            key_block = "/".join(block)

            if current_end_node.attributes["visited"]:
                break

            if key_block not in n_gram_trie:
                n_gram_trie[key_block] = -1
            
            node = n_gram_trie[key_block]
            current_count = 0
            if node != -1:
                current_count = node
            visits = trie[key].get_visits()
            n_gram_trie[key_block] = current_count + visits
            total_block_count += visits
            current_end_node.attributes["visited"] = True
            current_end_node = current_end_node.parent

    for key in for_key_in_trie(trie):
        node = trie[key]
        if "visited" in node.attributes:
            node.attributes["visited"] = False
    
    for key_n_gram in n_gram_trie.keys():
        block_count = n_gram_trie[key_n_gram]
        p = block_count / total_block_count
        acc -= p * math.log2(p)

    return acc