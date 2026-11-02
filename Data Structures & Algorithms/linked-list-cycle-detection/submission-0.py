# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
            if curr == fast:
                return True
        return False
