class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        r_hash = {}

        # Pass 1: Create a copy of every node
        while curr:
            r_hash[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Assign next and random pointers
        curr = head

        while curr:
            r_hash[curr].next = r_hash.get(curr.next)
            r_hash[curr].random = r_hash.get(curr.random)
            curr = curr.next

        return r_hash[head]