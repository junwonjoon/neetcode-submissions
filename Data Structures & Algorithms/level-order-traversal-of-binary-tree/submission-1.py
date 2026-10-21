# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = [root]
        levels = []
        while lst:
            level = []
            for _ in range(len(lst)):
                curr = lst.pop(0)
                if not curr:
                    continue
                lst.append(curr.left)
                lst.append(curr.right)
                level.append(curr.val)
            if level:
                levels.append(level)
        return levels
                