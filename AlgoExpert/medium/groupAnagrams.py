# -*- coding: utf-8 -*-
def groupAnagrams(strs: list) -> list:
    """
    49. 字母异位词分组
    ​# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
    # n is the length of the longest word
    """
    dct = {}
    
    for s in strs:
        k = tuple(sorted(s))
        if k not in dct:
            dct[k] = [s]
        else:
            dct[k].append(s)
    
    return list(dct.values())


from collections import defaultdict
def groupAnagrams(strs: list) -> list:
    """
    49. 字母异位词分组
    ​# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
    # n is the length of the longest word
    """
    dct = defaultdict(list)
    
    for word in strs:
        k = tuple(sorted(word))
        dct[k].append(word)
    
    return list(dct.values())
    
    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(strs)
