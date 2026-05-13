# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append([root, float('-inf')])
        res = 0

        while q:
            popped, max_val = q.pop()

            if popped.val >= max_val:
                res += 1
            
            if popped.left:
                q.append([popped.left, max(max_val, popped.val)])
            if popped.right:
                q.append([popped.right, max(max_val, popped.val)])
        
        return res