class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        zer0 = complexity[0]
        fac = 1
        for i in range(1,len(complexity)):
            if zer0 >= complexity[i] or complexity[i] < 1:
                return 0
            fac = (fac*i)%mod
        return fac