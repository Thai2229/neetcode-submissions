# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        next = curr.next

        while next:
            node = ListNode(math.gcd(curr.val,next.val))
            curr.next = node
            node.next = next
            curr = next
            next = next.next
        
        return head

