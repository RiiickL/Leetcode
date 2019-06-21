# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        val_set = set([])
        val_set.add(head.val)
        node_ptr = head
        next_ptr = head.next
        while(next_ptr != None):
            if next_ptr.val not in val_set:
                val_set.add(next_ptr.val)
                node_ptr.next = next_ptr
                node_ptr = next_ptr
            next_ptr = next_ptr.next
        node_ptr.next = None
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        