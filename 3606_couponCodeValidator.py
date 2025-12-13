class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        res = [[] for _ in range(4)]

        def valid_code(arg):
            if not arg:
                return False
            for i in arg:
                if not i.isalnum() and i != '_':
                    return False
            return True
        
        def valid_business(arg):
            if arg not in priority:
                return -1
            return priority[arg]
        
        for A, C in enumerate(code):
            if isActive[A] and valid_code(C) and (B:=valid_business(businessLine[A])) >= 0:
                res[B].append(C)
        
        return sorted(res[0])+sorted(res[1])+sorted(res[2])+sorted(res[3])