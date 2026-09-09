from _heapq import heapify
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_true = True

        def postorder_dfs(node):     
            nonlocal is_true       
            if not node or not is_true:
                return
            
            postorder_dfs(node.left)
            postorder_dfs(node.right)
            
            prev = node.val
            left_val = node.left.val if node.left else 0 
            right_val = node.right.val if node.right else 0

            node.val = 1 + max(left_val, right_val)
            if abs(left_val-right_val) > 1:
                is_true = False
            print(prev , node.val)

        postorder_dfs(root)
        
        return is_true

 