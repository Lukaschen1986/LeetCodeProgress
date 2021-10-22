# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([[root, 1]])
        count = 0

        while queue:
            curr_node, val = queue.popleft()
            count += 1

            if curr_node.left:
                queue.append([curr_node.left, 2*val])
            if curr_node.right:
                queue.append([curr_node.right, 2*val + 1])
            
        return count == val
