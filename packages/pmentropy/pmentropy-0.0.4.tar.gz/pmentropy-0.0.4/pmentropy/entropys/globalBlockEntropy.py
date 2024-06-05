from pmentropy.tools import for_key_in_trie
from pmentropy.Node import Node
import math
import multiprocessing 

def next_i(args):
    i, trie, total_block_count = args
    acc = 0.0
    n_gram_trie = {}
    is_visited = {}
    for key in for_key_in_trie(trie):
        depth = key.count("/") + 1
        if depth < i:
            continue

        current_end_node = trie[key]
        for _ in range(depth, i - 1, -1):
            if is_visited.get(current_end_node, False):
                break

            current_node = current_end_node
            block = ""
            for _ in range(i - 1, -1, -1):
                block += "/" + current_node.key
                current_node = current_node.parent
            block_key = block[1:]
            if block_key not in n_gram_trie:
                n_gram_trie[block_key] = current_end_node.get_visits()
            else:
                n_gram_trie[block_key] += current_end_node.get_visits()

            is_visited[current_end_node] = True
            current_end_node = current_end_node.parent
    

    for key_n_gram in n_gram_trie.keys():
        block_count = n_gram_trie[key_n_gram]
        p = block_count / total_block_count
        acc -= p * math.log2(p)
    return acc

def global_block_entropy(logs: tuple[dict[Node], dict]) -> float:
    trie, trie_infos = logs
    acc = 0.0
    longest_branch = trie_infos["longest_branch"]
    total_block_count = 0
    pool = multiprocessing.Pool()
    
    for node in trie_infos["end_nodes"]:
        depth = node.path.count("/") + 1
        total_block_count += (depth * (depth + 1)) * node.get_end_visits() / 2
    
    for val in pool.map(next_i, map(lambda i: (i, trie, total_block_count), range(longest_branch, 0, -1))):
        acc += val
    return acc