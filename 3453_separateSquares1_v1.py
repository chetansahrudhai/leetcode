class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high, area = float('inf'), float('-inf'), 0
        for x, y, l in squares:
            area += l*l
            low = min(low, y)
            high = max(high, y+l)
        crop = area/2.0
        for i in range(50):
            temp = 0
            mid = (low+high)/2.0
            for x, y, l in squares:
                Y = max(0, min(l, mid-y))
                temp += l*Y
            if temp < crop:
                low = mid
            else:
                high = mid
        return mid