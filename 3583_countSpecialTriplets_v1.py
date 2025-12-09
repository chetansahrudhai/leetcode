class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        greatest = max(nums) * 2
        freqPrev = [0] * (greatest + 1)
        freqNext = [0] * (greatest + 1)
        for i in nums: freqNext[i] += 1
        for i in nums:
            freqNext[i] -= 1
            trips = i * 2
            res = (res + freqPrev[trips] * freqNext[trips]) % mod
            freqPrev[i] += 1
        return res