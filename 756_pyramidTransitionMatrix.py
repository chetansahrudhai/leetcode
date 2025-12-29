class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pyramid = defaultdict(list)
        for triplet in allowed:
            parent = triplet[:2]
            child = triplet[2]
            pyramid[parent].append(child)
        
        @cache
        def dfs(i, word):
            if len(word) == 1:
                if len(i) == 1:
                    return True
                else:
                    return dfs('', i)
            super = word[:2]
            for sub in pyramid[super]:
                x = dfs(i+sub, word[1:])
                if x:
                    return True
            return False
        
        return dfs('', bottom)