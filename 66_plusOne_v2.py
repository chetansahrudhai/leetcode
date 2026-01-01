class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = str(digits)
        res = ''
        for i in digits:
            if i.isnumeric(): res += i
        res = int(res)
        res += 1
        return [int(i) for i in str(res)]