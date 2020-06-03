# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorderTraversal(root: TreeNode) -> list:
    # 前序：右 -> 左 -> 根
    white, grey = 0, 1
    stack = [(white, root)]
    res = []
    
    while stack:
        color, node = stack.pop()
        
        if not node:
            continue
        elif color == white:
            stack.append((white, node.right))
            stack.append((white, node.left))
            stack.append((grey, node))
        else:
            res.append(node.val)
    
    return res
            
    
if __name__ == "__main__":
    root = [1, None, 2, 3]
    root = TreeNode(root)
    preorderTraversal(root)
