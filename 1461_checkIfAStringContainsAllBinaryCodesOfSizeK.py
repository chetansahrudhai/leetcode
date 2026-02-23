class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        x = 2**k
        check = set()
        for i in range(n-k+1):
            temp = s[i:i+k]
            if temp not in check:
                check.add(temp)
                x -= 1
                if x==0:
                    return True
        return False