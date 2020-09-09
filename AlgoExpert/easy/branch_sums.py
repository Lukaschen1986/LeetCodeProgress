# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    """
    二叉树的分支和
    O(n) time | O(n) space
    """
    res = []
    
    def helper(node, runing_sum, res):
        if not node:
            return
        
        runing_new = runing_sum + node.value
        if (node.left is None) and (node.right is None):
            res.append(runing_new)
            return
        else:
            helper(node.left, runing_new, res)
            helper(node.right, runing_new, res)
    
    helper(root, 0, res)
    return res
