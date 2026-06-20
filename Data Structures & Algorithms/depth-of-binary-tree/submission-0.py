# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS:
        # if not root:
        #     return 0

        # depth = 0
        # stack = []
        # stack.append(root)

        # while stack:
        #     temp = stack.pop()
        #     print(temp.val)
        #     if temp.right:
        #         stack.append(temp.right)
        #     if temp.left:
        #         stack.append(temp.left)

        # BFS:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level



            
            
                
            

        