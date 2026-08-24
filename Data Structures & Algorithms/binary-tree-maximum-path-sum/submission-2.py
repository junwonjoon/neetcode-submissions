# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = -9999  
        def local_max(root, prev):
            nonlocal sol
            if not root:
                return
            prev_val = -9999
            if prev:
                prev_val = prev.val
            center = root.val
            left = 0 
            right = 0
            if root.left:
                left = root.left.val
            if root.right:
                right = root.right.val
            root.val = max(center + left, center, center + right)
            sol = max(sol, center, center + left, center + right, center + left + right)
        queue = deque([root]) 
        levels = [[(root, None)]]
        while queue:
            next_level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    next_level.append((curr.left, curr))
                if curr.right:
                    queue.append(curr.right)
                    next_level.append((curr.right, curr))
            levels.append(next_level)
        levels.pop()
        if len(levels) > 1:
            while levels:
                curr_level = levels.pop()
                for root, parent in curr_level:
                    local_max(root, parent)
                    print(sol, root.val)
        else:
            local_max(root, None)
        return sol