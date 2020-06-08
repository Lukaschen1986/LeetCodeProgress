# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        white, grey, depth = 0, 1, 0
        stack = [(white, root, depth)]
        res = []

        while stack:
            color, node, depth = stack.pop()

            if not node:
                continue
            elif color == white:
                stack.append((white, node.right, depth+1))
                stack.append((white, node.left, depth+1))
                stack.append((grey, node, depth))
            else:
                if len(res) == depth:
                    res.append([])
                res[depth].append(node.val)
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        
        return res
