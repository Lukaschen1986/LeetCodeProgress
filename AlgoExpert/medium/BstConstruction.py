# -*- coding: utf-8 -*-
class BST(object):
    """
    构建二叉查找树
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        curr_node = self
        while curr_node:
            if value < curr_node.value:
                if not curr_node.left:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
                    
            elif value > curr_node.value:
                if not curr_node.right:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right
            
            else:
                raise ValueError(f"the value {value} you inserted is equal to exsiting node.value")
        
        return self
    
    
    def contains(self, value):
        curr_node = self
        while curr_node:
            if value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                return True
        
        return False
    
    
    def remove(self, value, parentNode=None):
        """
        比较难
        """
        pass


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(5)
    bst.insert(2).insert(1)
    bst.insert(15)
    bst.contains(15)
