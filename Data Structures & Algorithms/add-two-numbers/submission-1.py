class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        curr = dummy
        p1, p2 = l1, l2

        while carry > 0 or p1 or p2:
            # Get the current digits, or 0 if a list has ended
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            value = v1 + v2 + carry

            # Update carry and the digit to store
            carry = value // 10
            value = value % 10

            # Add the digit to the result list
            curr.next = ListNode(value)
            curr = curr.next

            # Advance pointers if the lists haven't ended
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next