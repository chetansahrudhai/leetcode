class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        checked = []
        parLines = defaultdict(int)
        sameLines = defaultdict(int)
        parSides = defaultdict(int)
        sameSides = defaultdict(int)
        total = rhombuses = 0
        
        for x1, y1 in points:
            for x2, y2 in checked:
                dx = x1 - x2
                dy = y1 - y2
                
                if dx == 0:
                    k = "inf"
                    b = x1
                else:
                    k = dy / dx
                    b = y1 - k * x1
                    k = round(k, 8)
                    b = round(b, 8)
                
                slope = k
                line = (k, b)
                total += parLines[slope] - sameLines[line]
                parLines[slope] += 1
                sameLines[line] += 1

                side = dx * dx + dy * dy
                
                rhombuses += (parSides[(k, side)] - sameSides[(k, b, side)])
                
                parSides[(k, side)] += 1
                sameSides[(k, b, side)] += 1
            
            checked.append((x1, y1))
        
        return total - rhombuses // 2