# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            stack = [node]
            str_local = ""
            while stack:
                node = stack.pop()
                if node:
                    str_local += str(node.val)
                if node.left:
                    stack.append(node.left)
                    str_local += str(node.left.val)
                else:
                    str_local += "$"
                if node.right:
                    stack.append(node.right)
                    str_local += str(node.right.val)
                else:
                    str_local += "$"
            return str_local
        
        str_main = dfs(root)
        str_sub = dfs(subRoot)
        return True if str_sub in str_main else False
        
        
