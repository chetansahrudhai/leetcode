# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = best = 1
        bestSum = float('-inf')
        while queue:
            localSum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                localSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if localSum > bestSum:
                bestSum = localSum
                best = level
            level += 1
        return best