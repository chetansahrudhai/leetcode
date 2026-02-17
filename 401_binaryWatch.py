class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for H in range(12):
            for M in range(60):
                if (bin(H).count('1') + bin(M).count('1')) == turnedOn:
                    time = f"{H}:{M:02d}"
                    res.append(time)
        return res