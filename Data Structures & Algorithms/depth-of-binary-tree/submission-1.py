# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS:
        if not root:
            return 0

        depth = 1
        stack = [[root, depth]]

        while stack:
            temp_node, temp_depth = stack.pop()
            if temp_node:
                depth = max(depth, temp_depth)

            if temp_node.right:
                stack.append([temp_node.right, temp_depth + 1])
            if temp_node.left:
                stack.append([temp_node.left, temp_depth + 1])

        return depth

        # # BFS:
        # if not root:
        #     return 0

        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     level += 1

        # return level



            
            
                
            

        