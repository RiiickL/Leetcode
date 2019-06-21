# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        now = head
        while now!=None:
            node = now
            now = now.next
            
            node.next = pre
            pre = node
            
        return pre
     