class Solution:
    def hasAlternatingBits(self, n: int) -> bool:       
        res = n & 1
        while n != 0:
            n >>= 1
            if res == (n & 1):
                return False
            res = n & 1
        return True