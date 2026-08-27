# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -10000000001
        stopped = False

        def inOrder(node):
            nonlocal prev, stopped

            if not node:
                return

            inOrder(node.left)

            if prev >= node.val:
                stopped = True
            prev = node.val
            
            inOrder(node.right)

        inOrder(root)
        return not stopped