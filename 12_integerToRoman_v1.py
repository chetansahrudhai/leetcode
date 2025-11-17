class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        x = 0
        res = []
        while num > 0:
            n = num % 10
            if 1 <= n <= 3:
                res.append(ones[x] * n) 
            elif n == 4:
                res.append(ones[x] + fives[x])
            elif 5 <= n <= 8:
                res.append(fives[x] + ones[x] * (n - 5))
            elif n == 9:
                res.append(ones[x] + ones[x+1])
            x += 1
            num //= 10
        return "".join(res[::-1])