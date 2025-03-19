class Solution:
    def minOperations(self, nums: List[int]) -> int:
        L = len(nums)
        C = 0
        for i in range(L-2):
            if nums[i] == 0:
                nums[i] = nums[i] ^ 1
                nums[i+1] = nums[i+1] ^ 1
                nums[i+2] = nums[i+2] ^ 1
                C += 1
        return C if (nums[L-1]==1 and nums[L-2]==1) else -1