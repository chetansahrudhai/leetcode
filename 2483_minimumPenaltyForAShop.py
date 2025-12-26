class Solution:
    def bestClosingTime(self, customers: str) -> int:
        time = penalty = prefix = 0
        for i in range(len(customers)):
            prefix += -1 if customers[i]=='Y' else 1
            if prefix < penalty:
                time = i+1
                penalty = prefix
        return time