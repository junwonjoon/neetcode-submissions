# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if (node.val >= q.val or node.val >= p.val) and (node.val <= q.val or node.val <= p.val):
                return node
            stack.append(node.right)
            stack.append(node.left)

        


            
