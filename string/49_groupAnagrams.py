# -*- coding: utf-8 -*-
from collections import defaultdict

def groupAnagrams(strs: list) -> list:
    dct = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))
        dct[key].append(word)
    
    return list(dct.values())

    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(strs)
