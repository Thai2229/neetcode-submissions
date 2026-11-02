# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        l1 = l2 = fast = prev = head

        while fast and fast.next:
            prev = l2
            l2 = l2.next
            fast = fast.next.next
        
        prev.next = None
        prev = None

        while l2:
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node
        
        l2 = prev

        l1_curr, l2_curr = l1, l2
        while l2_curr:
            tmp1 = l1_curr.next
            tmp2 = l2_curr.next

            
            l1_curr.next = l2_curr

            if tmp1 is None:
                break
            l2_curr.next = tmp1

            l1_curr = tmp1
            l2_curr = tmp2



            
