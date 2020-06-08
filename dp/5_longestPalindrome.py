# -*- coding: utf-8 -*-
def longestPalindrome(s: str) -> str:
    dp = [[False]*len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True
    
    left = 0
    right = 1
    res = s[left:right]
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dp[i-1][i] = True
            left = i - 1
            right = left + 2
            res = s[left:right]
    
    for lens in range(3, len(s)+1):
        for i in range(0, len(s)-lens+1):
            j = i + lens - 1
            if (s[i] == s[j]) and dp[i+1][j-1]:
                dp[i][j] = True
                left = i
                right = left + lens
                res = s[left:right]
    
    return res


if __name__ == "__main__":
    s = "babad"
    longestPalindrome(s)
