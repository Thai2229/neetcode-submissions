"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        seen = {}

        curr = head
        while curr:
            seen[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            seen[curr].next = seen.get(curr.next)
            seen[curr].random = seen.get(curr.random)
            curr = curr.next
        
        return seen[head]