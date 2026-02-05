class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(0, len(nums)):
                res[i] = nums[(i + nums[i])%n]
        return res