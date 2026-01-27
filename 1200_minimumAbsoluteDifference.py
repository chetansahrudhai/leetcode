class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        A = len(arr)
        m = 2e6 + 1
        res = []
        arr.sort()
        for i in range(1, A):
            x = arr[i] - arr[i - 1]
            if x < m:
                m = x
                res = [[arr[i - 1], arr[i]]]
            elif x == m:
                res.append([arr[i - 1], arr[i]])
        return res