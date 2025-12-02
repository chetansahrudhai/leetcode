class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        groupY = {}
        for x, y in points:
            if y in groupY:
                groupY[y] += 1
            else:
                groupY[y] = 1
        numY = list(groupY.values())
        trapz = final = 0        
        for i in numY:
            if i >= 2:
                buffer = i * (i - 1) // 2
                trapz += buffer * final
                final += buffer    
        return trapz % mod