class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        n = len(s)
        s = [ord(letter) - ord('a') for letter in s]
        res = 0
        for x in range(n):
            if n - x <= res:
                break
            count = [0] * 26
            unique = frequency = 0
            for i in range(x, n):
                j = s[i]
                unique += count[j] == 0 
                count[j] += 1
                if count[j] > frequency:
                    frequency = count[j]
                current = i - x + 1
                if unique * frequency == current and current > res:
                    res = current
        return res