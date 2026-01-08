class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        store = {}

        def dp(i,j):
            if i == len(nums1) or j == len(nums2):
                return float("-inf")
            if (i,j) in store:
                return store[(i,j)]
            save = nums1[i] * nums2[j]
            res = max(save + dp(i+1, j+1), save, dp(i+1,j), dp(i,j+1))
            store[(i,j)] = res
            return store[(i,j)]

        return dp(0,0)