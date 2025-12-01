class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries)//n        
        while left < right:
            goal = right - (right - left)//2            
            addl = 0
            for charge in batteries:
                addl += min(goal, charge)
            if addl//n < goal:
                right = goal - 1
            else:
                left = goal
        return left
# went the binary search way, thank you hint-2.