class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        limit = left = 0
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            limit = max(limit, right - left + 1)
        return n - limit