# -*- coding: utf-8 -*-
def move_elements_to_end(nums, target):
    """
    将指定元素移动到列表的末尾
    # O(n) time | O(1) space
    """
    i = 0
    j = len(nums) - 1
    
    while i < j:
        if lst[j] == target:
            j -= 1
        else:
            if lst[i] == target:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            else:
                i += 1
    
    return nums
        
    
if __name__ == "__main__":
    import numpy as np
    np.random.randint(low=0, high=10, size=10).tolist()
    nums = [5, 0, 4, 1, 7, 5, 6, 3, 4, 8]
    target = 5
    move_elements_to_end(nums, target)
