# -*- coding: utf-8 -*-
def nthFibonacci(nth):
    """
    第n个斐波拉契数（递归）
    O(2^N) time | O(N) space
    """
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    else:
        return nthFibonacci(nth - 1) + nthFibonacci(nth - 2)


def nthFibonacci(nth, memorize={1:0, 2:1}):
    """
    第n个斐波拉契数（哈希）
    O(N) time | O(N) space
    """
    if nth in memorize:
        return memorize[nth]
    else:
        memorize[nth] = nthFibonacci(nth-1, memorize) + nthFibonacci(nth-2, memorize)
        return memorize[nth]
    

def nthFibonacci(nth):
    """
    第n个斐波拉契数（迭代）
    O(N) time | O(1) space
    """
    a = 0
    b = 1
    idx = 3
    
    while idx <= nth:
        a, b = b, a + b
        idx += 1
    
    return b



if __name__ == "__main__":
    nth = 10
