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
            itr_local = ""
            while stack:
                node = stack.pop()
                if node:
                    itr_local += str(node.val)
                if node.left:
                    stack.append(node.left)
                    itr_local += str(node.left.val)
                else:
                    itr_local += " "
                if node.right:
                    stack.append(node.right)
                    itr_local += str(node.right.val)
                else:
                    itr_local += " "
            return itr_local

        itr_main = dfs(root)
        itr_sub = dfs(subRoot)
        return True if itr_sub in itr_main else False
        
        
