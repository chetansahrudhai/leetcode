class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        def factor(x):
            res = 0
            d = 2
            while d * d < x:
                if x % d == 0:
                    if res > 0:
                        return 0
                    res += d + x // d
                d += 1
            if res == 0 or d * d == x:
                return 0
            return res + 1 + x
        
        for x in nums:
            res += factor(x)
        return res