# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global_max = 0

        def postOrder(node: Optional[TreeNode]):
            nonlocal global_max

            if not node:
                return

            postOrder(node.left)
            postOrder(node.right)

            max_left = node.left.val if node.left else 0
            max_right = node.right.val if node.right else 0
           
            node.val = max(max_left + 1, 1, max_right + 1)
            global_max = max(max_right + max_left + 1, global_max)

        postOrder(root)
        return global_max - 1