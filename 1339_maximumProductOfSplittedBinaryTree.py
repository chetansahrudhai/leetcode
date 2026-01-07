# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        self.res = 0

        def treeSum(node): # not threesome 'skull emoji' lol
            if not node:
                return 0
            return node.val + treeSum(node.left) + treeSum(node.right)
        
        total = treeSum(root)

        def DFS(node):
            if not node:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)
            subTreeSum = node.val + left + right
            self.res = max(self.res, subTreeSum * (total - subTreeSum))
            return subTreeSum
        
        DFS(root)
        return self.res % mod