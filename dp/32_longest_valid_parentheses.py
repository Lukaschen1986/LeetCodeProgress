# -*- coding: utf-8 -*-

def longestValidParentheses(s: str) -> int:
    if len(s) <= 1:
        return 0
    
    stack = [-1]
    res = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            res = max(res, i-stack[-1])
    
    return res


if __name__ == "__main__":
    s = ")()())"
    longestValidParentheses(s)
