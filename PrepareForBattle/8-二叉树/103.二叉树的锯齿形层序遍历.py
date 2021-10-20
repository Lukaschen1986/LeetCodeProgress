# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([[root, 0]])  # 
        res = []

        while queue:
            curr_node, depth = queue.popleft()
            if not curr_node:
                continue
            
            if len(res) == depth:  # 
                res.append([])
            
            res[depth].append(curr_node.val)
            queue.append([curr_node.left, depth + 1])
            queue.append([curr_node.right, depth + 1])
        
        for i in range(len(res)):
            if i % 2 == 1:  # 奇数层反转
                res[i] = res[i][::-1]
        
        return res
