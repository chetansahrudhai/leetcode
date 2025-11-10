class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            y = '-' + x[:0:-1]
        else:
            y = x[::-1]
        if (-2)**31 <= int(y) <= (2**31 -1):
            return int(y)
        else:
            return 0