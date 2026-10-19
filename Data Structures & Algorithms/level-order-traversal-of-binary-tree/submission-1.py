# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        trav = []
        q = deque([root])
        while q:
            level =  []
            for _ in range(len(q)):
                nd = q.popleft()
                if nd:
                    level.append(nd.val)
                    q.append(nd.left)
                    q.append(nd.right)
            if level:
                trav.append(level)
        return trav

                    

        