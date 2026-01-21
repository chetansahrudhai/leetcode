class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num == 2:
                res.append(-1)
                continue
            n = num
            x = 0
            while num & 1 == 1:
                x += 1
                num >>= 1
            res.append(n - 2 ** (x-1))
        return res