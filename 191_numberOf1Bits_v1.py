class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            if (n >> i) & 1:
                total += 1
        return total