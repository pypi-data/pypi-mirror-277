import string
from Node import Node

alphabet = string.ascii_letters + string.digits 

def number_to_alphabet(number: int) -> str:
    base = len(alphabet)
    result = ""
    while number:
        q, r= divmod(number, base)
        result += alphabet[r]
        number = q
    return result[::-1] or alphabet[0]

def add_mapping_key(mapping: dict, name: str) -> None:
    char = mapping.get(name)
    if char is not None:
        return char
    char = number_to_alphabet(len(mapping))
    mapping[name] = char
    return char


def increment_trie(trie: dict, key: str, parent = None) -> None:
    if key in trie:
        node = trie[key]
        node.increment_visits()
        return node
    else:
        node = Node(key, 1, 0, parent)
        trie[key] = node
        return node

def increment_end_trie(trie: dict, trie_infos: dict, key: str, parent = None) -> None:
    if key in trie:
        node = trie[key]
        if not node.is_end_node():
            trie_infos["end_nodes"].append(node)
        trie[key].increment_end_visits()
    else:
        node = Node(key, 0, 1, parent)
        trie[key] = node
        trie_infos["end_nodes"].append(node)
        return node

def min_index(*a):
    min_value = a[0]
    min_index = 0
    for i, el in enumerate(a):
        if el < min_value:
            min_value = el
            min_index = i
    return min_index

def minimum(values: list, n: int):
    n = len(values) if n > len(values) else n

    result = [float("inf")] * n

    for v in values:
        for i in range(0, n):
            
            if v < result[i]:
                
                for j in range(n - 1, i, - 1):
                    result[j] = result[j-1]
                
                result[i] = v
                break
    return result

def for_key_in_trie(trie):
    return trie.keys()