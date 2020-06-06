# -*- coding: utf-8 -*-
def generateParenthesis(n: int) -> list:
    res = []
    nums = n*2
    left = 0
    right = 0
    
    def track_back(combination, left, right):
        if len(combination) == nums:
            res.append(combination)
        else:
            if left < n:
                track_back(combination + "(", left + 1, right)
            if right < left:
                track_back(combination + ")", left, right + 1)
    
    track_back("", left, right)
    return res
            
    
if __name__ == "__main__":
    n = 3
    generateParenthesis(n)
