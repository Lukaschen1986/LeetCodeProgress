# -*- coding: utf-8 -*-
class MinMaxStack(object):
    """
    构造最小最大栈
    """
    def __init__(self):
        self.__stack = []
        self.__min_max_stack = []
    
    
    def peek(self):
        """O(1) time | O(1) space"""
        if not self.__stack:
            raise IndexError("list index out of range")
        return self.__stack[-1]
    
    
    def pop(self):
        """O(1) time | O(1) space"""
        if not self.__stack:
            raise IndexError("list index out of range")
        self.__min_max_stack.pop()
        return self.__stack.pop()
    
    
    def push(self, num):
        """O(1) time | O(1) space"""
        if (not isinstance(num, int)) or (not isinstance(num, float)):
            raise TypeError("push must be INT or FLOAT")
        running_min_max = {"min": num, "max": num}
        
        if self.__min_max_stack:
            last_min_max = self.__min_max_stack[-1]
            running_min_max["min"] = min(running_min_max.get("min"), last_min_max.get("min"))
            running_min_max["max"] = max(running_min_max.get("max"), last_min_max.get("max"))
            
        self.__stack.append(num)
        self.__min_max_stack.append(running_min_max)
        return
    
    
    def get_min(self):
        """O(1) time | O(1) space"""
        if not self.__min_max_stack:
            raise IndexError("list index out of range")
        return self.__min_max_stack[-1].get("min")
    
    
    def get_max(self):
        """O(1) time | O(1) space"""
        if not self.__min_max_stack:
            raise IndexError("list index out of range")
        return self.__min_max_stack[-1].get("max")
    
    
    @property
    def stack(self):
        """O(1) time | O(1) space"""
        return self.__stack


if __name__ == "__main__":
    mms = MinMaxStack()
    mms.stack # []
    
    mms.push(1)
    mms.push("3")
    mms.push(7)
    mms.push(5)
    mms.stack # [1, 7, 5]
    
    mms.peek() # 5
    mms.stack # [1, 7, 5]
    
    mms.pop() # 5
    mms.stack # [1, 7]
    
    mms.get_min() # 1
    mms.get_max() # 7
    
