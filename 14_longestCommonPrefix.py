class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any(i == "" for i in strs):
            return ""
        res = strs[0]
        check = strs[0][0]
        if not all(i[0] == check for i in strs):
            return ""
        for i in strs:
            while not i.startswith(res):
                res = res[:-1]
        return res