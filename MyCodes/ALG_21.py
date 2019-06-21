# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val<l2.val:
            p = l1
            pn = p
            l1 = l1.next
        else:
            p = l2
            pn = p
            l2 = l2.next
        
        while((l1 is not None) and (l2 is not None)):
            if l1.val<l2.val:
                pn.next = l1
                pn = pn.next
                l1 = l1.next
            else:
                pn.next = l2
                pn = pn.next
                l2 = l2.next
            
        if l1 is None:
            pn.next = l2
        
        if l2 is None:
            pn.next = l1
        
        return p
        
        
        