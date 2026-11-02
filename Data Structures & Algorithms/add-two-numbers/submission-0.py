class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        curr1, curr2 = l1, l2 

        while curr1:
            num1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            num2.append(curr2.val)
            curr2 = curr2.next
        
        num1 = int(''.join(map(str, num1[::-1])))
        num2 = int(''.join(map(str, num2[::-1])))
        result = num1 + num2

        dummy = ListNode(0)   # dummy head
        curr = dummy          # pointer to build list

        for digit in str(result)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
