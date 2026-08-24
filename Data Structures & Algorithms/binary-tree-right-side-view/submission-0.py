# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        lst_to_return = [root.val]
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            right = return_right_view(queue.copy())
            if right:
                lst_to_return.append(right)
        return lst_to_return 

def return_right_view(lst):
    while lst:
        curr = lst.pop()
        if curr:
            return curr.val