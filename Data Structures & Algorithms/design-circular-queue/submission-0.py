class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        # Sentinels
        self.left = Node()   # front sentinel
        self.right = Node()  # rear sentinel
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = Node(value, self.right, self.right.prev)
        self.right.prev.next = cur
        self.right.prev = cur
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        front = self.left.next
        self.left.next = front.next
        front.next.prev = self.left
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.next.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.prev.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
