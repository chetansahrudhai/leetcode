class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = k = res = -inf
        for num in range(1, n):
            n0 = nums[num - 1]
            n1 = nums[num]
            x = y = z = -inf
            if n0 < n1:
                x = max(n0 + n1, i + n1)
                z = max(k + n1, j + n1)
            elif n0 > n1:
                y = max(j + n1, i + n1)
            res = max(res, z)
            i, j, k = x, y, z
        return res