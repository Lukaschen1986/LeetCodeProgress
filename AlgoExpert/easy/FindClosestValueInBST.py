# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def FindClosestValueInBST(root, target):
    """
    二叉查找树中最接近的值（递归）
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    """
    closest = float("inf")
    
    def helper(node, target, closest):
        if not node:
            return closest
        else:
            if abs(target - node.value) < abs(target - closest):
                closest = node.value
            if target > closest:
                helper(node.right, target, closest)
            elif target < closest:
                helper(node.left, target, closest)
            else:
                return closest
    
    closest = helper(root, target, closest)
    return closest


def FindClosestValueInBST(root, target):
    """
    二叉查找树中最接近的值（迭代）
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    """
    closest = float("inf")
    current_node = root
    
    while current_node:
        if abs(target - current_node.value) < abs(target - closest):
            closest = current_node.value
            
        if target > closest:
            current_node = current_node.right
        elif target < closest:
            current_node = current_node.left
        else:
            break
    
    return closest
