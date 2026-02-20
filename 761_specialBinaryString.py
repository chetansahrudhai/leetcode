class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        x = count = 0
        res = []
        for i in range(len(s)):
            count += 1 if s[i]=='1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[x+1:i]) + '0')
                x = i + 1
        res = sorted(res, reverse = True)
        return ''.join(res)