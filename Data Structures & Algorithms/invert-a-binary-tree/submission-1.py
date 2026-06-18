# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # recursive solutio:
        # if not root:
        #     return None

        # tmp = root.left
        # root.left = root.right
        # root.right = tmp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # not recursive solution:
        if not root: return
        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()
            left = curr.left
            curr.left = curr.right
            curr.right = left
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return root
