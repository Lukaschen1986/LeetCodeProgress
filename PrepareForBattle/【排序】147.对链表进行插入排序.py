# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:32:25 2021

@author: ASUS
"""
def ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


def insertionSortList(head):
    """
    ​O(N^2) time | O(1) space
    """
    if not head:
        return head
    
    dumm = ListNode(0)
    dumm.next = head
    last = head
    curr = head.next
    
    while curr:
        if last.val <= curr.val:
            last = last.next
        else:
            prev = dumm
            while prev.next.val <= curr.val:
                prev = prev.next
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
        curr = last.next
    
    return dumm.next
