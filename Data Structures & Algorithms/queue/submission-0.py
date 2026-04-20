class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
      
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail


    def append(self, value: int) -> None:
        node = Node(value)
        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node


    def pop(self) -> int:
        if self.isEmpty():
            return -1

        node = self.tail.prev
        prev = node.prev

        prev.next = self.tail
        self.tail.prev = prev

        node.prev = None
        node.next = None

        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        node = self.head.next
        nxt = node.next

        self.head.next = nxt
        nxt.prev = self.head

        node.prev = None
        node.next = None

        return node.val