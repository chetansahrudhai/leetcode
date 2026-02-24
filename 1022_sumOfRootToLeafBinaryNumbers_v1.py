# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, i):
            if not node:
                return 0
            i = 2*i + node.val
            if not node.left and not node.right:
                return i
            return dfs(node.left, i) + dfs(node.right, i)
        return dfs(root, 0)