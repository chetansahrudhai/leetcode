class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])
        res = greater = 0
        limit = []
        for starting, ending, value in events:
            greater = max(greater, value)
            limit.append((ending, greater))
        for starting, ending, value in events:
            res = max(res, value)
            x = bisect.bisect_left(limit, (starting, 0)) - 1
            if x >= 0:
                res = max(res, value + limit[x][1])
        return res