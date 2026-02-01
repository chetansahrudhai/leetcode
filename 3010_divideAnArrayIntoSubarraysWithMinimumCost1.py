class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        else:
            if nums == sorted(nums):
                return sum(nums[:3])
            else:
                n = nums[1:]
                n.sort()
                i1, i2 = n[0], n[1]
                i1 = nums.index(i1)
                i2 = nums.index(i2)
                return nums[0] + nums[i1] + nums[i2]