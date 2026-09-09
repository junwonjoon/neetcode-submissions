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

        def DFS_sanitize(node):     
            nonlocal is_true       
            if not node:
                return
            
            DFS_sanitize(node.left)
            DFS_sanitize(node.right)
            
            prev = node.val
            left_val = node.left.val if node.left else 0 
            right_val = node.right.val if node.right else 0

            node.val = 1 + max(left_val, right_val)
            if abs(left_val-right_val) > 1:
                is_true = False
            print(prev , node.val)


        # def DFS_check(node):
        #     nonlocal is_true

        #     if not node:
        #         return
            
        #     DFS_check(node.left)
        #     DFS_check(node.right)

        #     val1 = node.left.val if node.left else 0
        #     val2 = node.right.val if node.right else 0

        #     if val1 + val2 + node.val >= 1:
        #         is_true = False

        DFS_sanitize(root)
        # DFS_check(root)
        
        return is_true

 