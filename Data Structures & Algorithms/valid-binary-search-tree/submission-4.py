# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root, float('-inf'), float('inf')])

        while q:
            node, left, right = q.popleft()
            if node:
                if not left < node.val < right:
                    return False
                q.append([node.left, left, node.val])
                q.append([node.right, node.val, right])
        return True