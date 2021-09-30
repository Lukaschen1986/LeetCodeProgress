class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        i = j = 0

        while (j < n) and (i <= j):
            tmp = s[i:j+1]
            if len(tmp) == len(set(tmp)):
                res = max(res, len(tmp))
                j += 1
            else:
                i += 1
        
        return res
