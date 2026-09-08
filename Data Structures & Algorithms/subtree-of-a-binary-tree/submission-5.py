# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        lst_main = []
        lst_sub = []

        def dfs(node, lst):
            stack = [node]
            while stack:
                node = stack.pop()
                if node:
                    lst.append(node.val)
                if node.left:
                    stack.append(node.left)
                    lst.append(node.left.val)
                else:
                    lst.append(None)
                if node.right:
                    stack.append(node.right)
                    lst.append(node.right.val)
                else:
                    lst.append(None)
        
        dfs(root, lst_main)
        dfs(subRoot, lst_sub)
        count = 0
        i = 0
        j = 0
        max_count = 0
        len_sub = len(lst_sub)
        while i < len(lst_main):
            if j >= len_sub:
                return True
            if lst_main[i] == lst_sub[j]:
                count += 1
                i += 1
                j += 1
            else:
                i += 1
                j = 0
                count = 0
            max_count = max(max_count, count)
        

        return any(lst_main[i : i + len(lst_sub)] == lst_sub for i in range(len(lst_main) - len(lst_sub) + 1))
