# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()
            if getVal(curr_p) != getVal(curr_q):
                return False
            if not curr_p and not curr_q:
                continue
            if getVal(curr_p.left) == getVal(curr_q.left) and getVal(curr_p.right) == getVal(curr_q.right):
                stack_p.append(curr_p.left)
                stack_p.append(curr_p.right)
                stack_q.append(curr_q.left)
                stack_q.append(curr_q.right)
            else:
                return False
        return True

def getVal(tree: Optional[TreeNode]) -> int:
    return tree.val if tree else -999               