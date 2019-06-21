# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        res = l1
        
        while((l1 is not None) and (l2 is not None)):
            sum = l1.val + l2.val + add
            l1.val = sum%10
            add = sum//10
            l1_last = l1
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            sum = l1.val + add
            l1.val = sum%10
            add = sum//10
            l1_last = l1
            l1 = l1.next
            if add==0:
                break
        
        if l2 is not None:
            l1_last.next = l2
            while l1_last.next is not None:
                sum = l2.val + add
                l2.val = sum%10
                add = sum//10
                l1_last = l2
                l2 = l2.next
                if add==0:
                    break
        
        if add==1:
            l1_last.next = ListNode(1)
        
        return res
        
        
        
        
        
        
        
        
        