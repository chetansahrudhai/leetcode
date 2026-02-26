class Solution:
    def numSteps(self, s: str) -> int:
        count = x = 0
        for i in range(len(s) - 1, 0, -1):
            if (((s[i] == '1') + x) & 1):
                count += 2
                x = 1
            else:
                count += 1
        return count + x