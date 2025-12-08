class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i*i for i in range(1, n+1)}
        res = 0
        for i in range(1, n+1):
            buffer = i*i
            for j in range(i+1, n+1):
                check = buffer + j*j
                if check in squares:
                    res += 2  
        return res