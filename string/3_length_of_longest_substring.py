# -*- coding: utf-8 -*-
def lengthOfLongestSubstring(s: str) -> int:
    stack = []
    max_len = 0
    
    for x in s:
        if x not in stack:
            stack.append(x)
        else:
            stack = stack[stack.index(x)+1:]
            stack.append(x)
        max_len = max(max_len, len(stack))
    
    return max_len


if __name__ == "__main__":
    s = "abcabcbb"
    lengthOfLongestSubstring(s)
