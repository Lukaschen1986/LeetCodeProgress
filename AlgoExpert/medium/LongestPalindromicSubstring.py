# -*- coding: utf-8 -*-
def longest_palindromic_substring(s):
    """
    5.最长回文子串
    ​# O(N^2) time | O(1) space
    """
    curr_idx = [0, 1]
    
    for i in range(1, len(s)):
        odd_idx = get_longest_idx(s, i-1, i+1)
        even_idx = get_longest_idx(s, i-1, i)
        
        local_idx = max(odd_idx, even_idx, key=lambda x: x[1] - x[0])
        curr_idx = max(curr_idx, local_idx, key=lambda x: x[1] - x[0])
    
    return s[curr_idx[0]: curr_idx[1]]
        
        
def get_longest_idx(s, idx_l, idx_r):
    while (idx_l >= 0) and (idx_r < len(s)):
        if s[idx_l] != s[idx_r]:
            break
        else:
            idx_l -= 1
            idx_r += 1
        
    return [idx_l+1, idx_r]
    
    
    
if __name__ == "__main__":
    s = "abaxyzzyxf"
    longest_palindromic_substring(s)
