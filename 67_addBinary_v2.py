class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = int(a, 2), int(b, 2)
        while j:
            i, j = i ^ j, (i & j) << 1
        return format(i, 'b')