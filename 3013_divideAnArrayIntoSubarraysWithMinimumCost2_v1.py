class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        res = float('inf')
        k -= 2
        cost = nums.pop(0)
        X = SortedList(nums[:dist])
        cost += sum(X[:k])
        for i, j in zip(nums, nums[dist:]):
            X.add(j)
            cost += min(X[k], j)
            res = min(res, cost)
            cost -= min(X[k], i)
            X.remove(i)
        return res