# -*- coding: utf-8 -*-
from collections import deque

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def invert_binary_tree(root):
    """
    二叉树的镜像（递归）
    # O(n) time | O(log(n)) space
    """
    if not root:
        return
    else:
        root.left, root.right = root.right, root.left
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)
    

def invert_binary_tree(root):
    """
    二叉树的镜像（迭代：广度优先搜索）
    # O(n) time | O(n) space
    """
    queue = deque([root])
    
    while queue:
        curr_node = queue.popleft()
        
        if not curr_node:
            continue
        
        curr_node.left, curr_node.right = curr_node.right, curr_node.left
        queue.append(curr_node.left)
        queue.append(curr_node.right)
    
    return
