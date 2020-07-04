# -*- coding: utf-8 -*-
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        y = str(x)[::-1]
        return y == str(x)



if __name__ == "__main__":
    x = -121
    x = 120
    isPalindrome(x)
