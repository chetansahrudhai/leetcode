class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            if i in nums[x+1:]:
                return i
            x += 1