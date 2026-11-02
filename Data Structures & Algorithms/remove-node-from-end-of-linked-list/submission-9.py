# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        fast = head
        prev = None

        #updating fast to the current correct pointer
        for i in range(n):
            fast = fast.next
        
        #handles the edge case of n = length of list
        if not fast: 
            return head.next

        while fast:
            prev = curr
            curr = curr.next
            fast = fast.next
        
        prev.next = curr.next
        return head

        
        
