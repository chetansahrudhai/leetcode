class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_num = 0
        for i in nums:
            xor_num ^= i
        return xor_num