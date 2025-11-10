class Solution:
    def reverse(self, x: int) -> int:
        Pos = x > 0
        x = abs(x)
        Rev = int(str(x)[::-1])
        if Rev >= 2**31 - 1: return 0
        return Rev if Pos else -Rev