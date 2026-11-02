# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #key intuition, merge each list one at a time, merge list 1 with list 2
        #and take the result of that merge it with list 3 and so on
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            # attach whatever is left
            if l1:
                tail.next = l1
            else:
                tail.next = l2

            return dummy.next
        
        for i in range(1,len(lists)):
            merged = mergeTwoLists(lists[i],lists[i-1])
            lists[i] = merged
        
        return lists[-1]
                        



    