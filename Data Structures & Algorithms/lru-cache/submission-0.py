class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # remove node from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # move to MRU (right side)
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        return node.value

    def put(self, key: int, value: int) -> None:

        # if key already exists, remove old node first
        if key in self.cache:
            old = self.cache[key]

            old.prev.next = old.next
            old.next.prev = old.prev

            del self.cache[key]

        node = Node(key, value)
        self.cache[key] = node

        # insert at MRU (before right)
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        # evict if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next

            self.left.next = lru.next
            lru.next.prev = self.left

            del self.cache[lru.key]