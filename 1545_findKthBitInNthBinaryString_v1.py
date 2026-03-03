class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bs = ["0"]
        for i in range(1,21):
            x = bs[i-1] + "1"
            y = bs[i-1].replace('1', '2').replace('0', '1').replace('2', '0')
            y = y[::-1]
            x += y
            bs.append(x)
        return bs[n-1][k-1]