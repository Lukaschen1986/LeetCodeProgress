# -*- coding: utf-8 -*-
def reverse(x: int) -> int:
    if x < 0:
        y = -int(str(-x)[::-1])
    else:
        y = int(str(x)[::-1])
    
    if (y < -2**31) or (y > 2**31-1):
        return 0
    
    return y



if __name__ == "__main__":
    x = -123
    x = 120
    reverse(x)
