# -*- coding: utf-8 -*-
class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth_node_from_end(head, k):
    """
    删除倒数第n个结点
    # O(n) time | O(1) space
    """
    first = head
    second = head
    counter = 1
    
    while counter <= k:
        second = second.next
        counter += 1
    
    # 场景1
    if not second:
        head.value = head.next.value # 这一步没搞懂
        head.next = head.next.next
        return 
    
    # 场景2
    while second.next is not None:
        first = first.next
        second = second.next
    
    first.next = first.next.next
    return 
