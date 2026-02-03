class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4 or nums[0] >= nums[1]:
            return False
        switch, flow = 0, 1
        for i in range(1, len(nums)):
            if flow * nums[i - 1] > flow * nums[i]:
                switch = switch + 1
                flow = flow * -1
            if nums[i - 1] == nums[i] or switch > 2:
                return False
        return switch == 2