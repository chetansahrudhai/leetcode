class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        res = 0
        left, right = 1, len(cells)
        
        def crossable(day):
            grid = [[0] * col for _ in range(row)]
            queue = deque()
            visited = [[False] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i][0] - 1, cells[i][1] - 1
                grid[r][c] = 1
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited[0][c] = True
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                for rDir, cDir in dirs:
                    rNext, cNext = r + rDir, c + cDir
                    if 0 <= rNext < row and 0 <= cNext < col and not visited[rNext][cNext] and grid[rNext][cNext] == 0:
                        visited[rNext][cNext] = True
                        queue.append((rNext, cNext))
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if crossable(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res