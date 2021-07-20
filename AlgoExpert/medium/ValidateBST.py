# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:02:45 2021

@author: ASUS
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def validate_bst(root):
    stack = [(root, float("-inf"), float("inf"))]
    
    while stack:
        node, min_val, max_val = stack.pop()
        
        if not node:
            continue
        if (node.val <= min_val) or (node.val >= max_val):
            return False
        
        stack.append((node.left, min_val, node.val))
        stack.append((node.right, node.val, max_val))
    
    return True
