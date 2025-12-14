class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        res = 1
        previous = seats = 0
        for current, i in enumerate(corridor):
            if i == 'S':
                seats += 1
                if seats > 2 and seats % 2 == 1:
                    res *= current - previous
                previous = current
        if seats > 1 and seats % 2 == 0:
            return res % mod
        else:
            return 0