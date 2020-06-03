# -*- coding: utf-8 -*-
def letterCombinations(digits: str) -> list:
    phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
    res = []
    
    def track_back(combination, digits):
        if not digits:
            res.append(combination)
        else:
            for x in phone.get(digits[0]):
                track_back(combination + x, digits[1:])
    
    track_back("", digits)
    return res


if __name__ == "__main__":
    digits = "234"
    letterCombinations(digits)
