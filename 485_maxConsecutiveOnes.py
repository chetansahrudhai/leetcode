class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        w1,w2 = 0,0
        for i in nums:
            if i == 1:
                w1 += 1
            elif i == 0:
                w1 = 0
            if w1 > w2:
                w2 = w1
        return w2