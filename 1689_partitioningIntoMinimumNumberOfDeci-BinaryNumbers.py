class Solution:
    def minPartitions(self, n: str) -> int:
        check = [9,8,7,6,5,4,3,2,1]
        for i in check:
            if str(i) in n:
                return i