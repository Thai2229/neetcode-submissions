# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        res = ListNode(0, None)
        dummy = res

        while curr_1 or curr_2:
            if not curr_1:
                res.next = curr_2
                res = res.next
                curr_2 = curr_2.next
            elif not curr_2:
                res.next = curr_1
                res = res.next
                curr_1 = curr_1.next
            else:
                if curr_1.val < curr_2.val:
                    res.next = curr_1
                    res = res.next
                    curr_1 = curr_1.next
                else:
                    res.next = curr_2
                    res = res.next
                    curr_2 = curr_2.next

        return dummy.next