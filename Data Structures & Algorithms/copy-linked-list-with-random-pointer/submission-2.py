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
        nodeMap = {}
        ptr = head
        while ptr:
            nodeMap[ptr] = Node(ptr.val)
            ptr = ptr.next
        for old, new in nodeMap.items():
            nxt = old.next
            if nxt:
                new.next = nodeMap[nxt]
            rnd = old.random
            if rnd:
                new.random = nodeMap[rnd]
        return nodeMap[head] if head else None
        

        