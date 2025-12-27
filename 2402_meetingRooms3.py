class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        busy = []
        free = list(range(n))
        count = [0] * n
        heapq.heapify(free)
        for start, end in meetings:
            diff = end - start
            while busy and busy[0][0] <= start:
                x, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                time, room = heapq.heappop(busy)
                heapq.heappush(busy, (time + diff, room))
                count[room] += 1
        return count.index(max(count))