# -*- coding: utf-8 -*-
def longestCommonPrefix(strs: list) -> str:
    res = ""
    
    for (idx, zips) in enumerate(zip(*strs)):
        if (idx == 0) and len(set(zips)) != 1:
            return ""
        elif len(set(zips)) == 1:
            res += zips[0]
    
    return res
    
    
    
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]
    strs = ["aca","cba"]
    longestCommonPrefix(strs)
