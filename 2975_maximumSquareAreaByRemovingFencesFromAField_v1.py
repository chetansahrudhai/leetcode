class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        S = set()
        mod = 10**9+7
        res = 0
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                S.add(abs(hFences[j]-hFences[i]))
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                x = abs(vFences[j]-vFences[i])
                if x in S:
                    res = max(res, x)
        if res == 0: return -1
        return (res*res)%mod