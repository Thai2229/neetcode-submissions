# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count total list length
        #count - n + 1

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        count = count - n + 1
        untilDel = 1
        curr = head
        prev = None

        while untilDel != count:
            untilDel += 1
            prev = curr
            curr = curr.next
        
        if not prev: return curr.next
        prev.next = curr.next
        return head
        




        
