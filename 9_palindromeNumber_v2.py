import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        n = floor(log10(x)) + 1
        while n>1:
            if x//(10**(n-1)) != x%10:
                return False
            x = (x % (10 ** (n - 1))) // 10
            n -= 2
        return True