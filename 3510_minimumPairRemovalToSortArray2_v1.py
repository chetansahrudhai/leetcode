class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        left = list(range(-1, N - 1))
        right = list(range(1, N + 1))
        self.count = sum(nums[i] > nums[i + 1] for i in range(N - 1))
        x = SortedList([nums[i] + nums[i + 1], i] for i in range(N - 1))
        
        def add(u):
            v = right[u]
            if 0 <= u < v < N:
                x.add([nums[u] + nums[v], u])
                self.count += nums[u] > nums[v]

        def remove(u):
            v = right[u]
            if 0 <= u < v < N:
                x.discard([nums[u] + nums[v], u])
                self.count -= nums[u] > nums[v]

        while self.count:
            res += 1
            _, u = x.pop(0)
            v = right[u]
            i, j = left[u], right[v]
            remove(i)
            remove(u)
            remove(v)
            nums[u] += nums[v]
            right[u] = j
            if j < N:
                left[j] = u
            add(i)
            add(u)
        return res