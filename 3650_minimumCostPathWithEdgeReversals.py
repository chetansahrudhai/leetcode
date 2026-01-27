class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        A = defaultdict(list)
        for i, j, k in edges:
            A[i].append((j, k))
            A[j].append((i, 2 * k))
        distance = [math.inf] * n
        distance[0] = 0
        heap = [(0, 0)]
        while heap:
            d, i = heapq.heappop(heap)
            if i == n - 1:
                return d
            if d != distance[i]:
                continue
            for j, k in A[i]:
                if distance[i] + k < distance[j]:
                    distance[j] = distance[i] + k
                    heapq.heappush(heap, (distance[j], j))
        return -1