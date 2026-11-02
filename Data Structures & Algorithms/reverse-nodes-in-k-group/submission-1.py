# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #first count if there are k nodes left, if there aren't, simply return the head
        #then reverse the next k nodes
        node = head

        # check if enough nodes
        for _ in range(k):
            if not node:
                return head
            node = node.next

        # reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # connect
        head.next = self.reverseKGroup(curr, k)

        return prev
