class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while True:
            order = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    order = False
                    break
            if order:
                return res
            minisum = -1
            x = -1
            for i in range(len(nums) - 1):
                currsum = nums[i] + nums[i + 1]
                if x == -1 or currsum < minisum:
                    minisum = currsum
                    x = i
            nums[x] = minisum
            del nums[x + 1]
            res += 1