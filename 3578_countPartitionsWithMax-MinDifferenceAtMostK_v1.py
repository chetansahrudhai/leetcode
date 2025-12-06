class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        L = len(nums)
        DP = [0]*(L+1)
        DP[0] = 1
        Pre = [0]*(L+1)
        Pre[0] = DP[0]
        minDP = deque()
        maxDP = deque()
        left = 0
        for idx in range(L):
            while maxDP and nums[maxDP[-1]]<=nums[idx]: maxDP.pop()
            maxDP.append(idx)
            while minDP and nums[minDP[-1]] > nums[idx]: minDP.pop()
            minDP.append(idx)
            while nums[maxDP[0]] - nums[minDP[0]] > k:
                if maxDP[0] == left:
                    maxDP.popleft()
                if minDP[0] == left:
                    minDP.popleft()
                left+=1 
            if left == 0: total = Pre[idx]
            else: total = (Pre[idx] - Pre[left - 1]) % mod
            DP[idx+1] = total
            Pre[idx+1] = (Pre[idx] + DP[idx+1])%mod
        return DP[L]%mod