# -*- coding: utf-8 -*-
def plusOne(digits: list) -> list:
    n = int("".join(str(x) for x in digits)) + 1
    s = str(n)
    return [int(c) for c in s]
    

if __name__ == "__main__":
    digits = [4,3,2,1]
    digits = [9]
    plusOne(digits)
