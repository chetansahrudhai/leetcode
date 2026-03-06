class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '0' not in s:
            return True
        x = s.find('0')
        s = s[x:]
        if '1' in s:
            return False
        else:
            return True