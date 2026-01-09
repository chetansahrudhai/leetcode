# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, level = 0):
            if not node:
                return level - 1
            L, R = dfs(node.left, level + 1), dfs(node.right, level + 1)
            if L == R:
                deepest[L] = node
            return max(L,R)
        deepest = {}
        return deepest[dfs(root)]