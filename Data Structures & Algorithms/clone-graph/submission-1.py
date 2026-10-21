"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        origToCopy = {}
        def create_copy(node):
            if node in origToCopy:
                return origToCopy[node]
            copy = Node(node.val)
            origToCopy[node] = copy
            for v in node.neighbors:
                copy.neighbors.append(create_copy(v))
            return copy
        return create_copy(node)
        
