class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2]!=0 and nums[p1]==0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            if nums[p1]!=0:
                p1+=1