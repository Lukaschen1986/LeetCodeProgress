# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        depth = 1
        num = 1
        queue = deque([[root, depth, num]])  # slzb
        width = 0

        while queue:
            if queue[-1][1] == queue[0][1]:  # slzb, 判断深度是否一致
                width = max(width, queue[-1][2] - queue[0][2] + 1)  # slzb, 更新最大宽度

            curr_node, depth, num = queue.popleft()
            if curr_node.left:
                queue.append([curr_node.left, depth + 1, 2*num])
            if curr_node.right:
                queue.append([curr_node.right, depth + 1, 2*num + 1])
            
        
        return width
