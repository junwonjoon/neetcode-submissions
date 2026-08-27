# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -10000000001
        break_ = False

        def inOrder(node):
            nonlocal prev, break_

            if not node or break_:
                return
            
            inOrder(node.left)
            if prev >= node.val:
                break_ = True
            prev = node.val
            inOrder(node.right)

        inOrder(root)

        if break_:
            return False
        return True