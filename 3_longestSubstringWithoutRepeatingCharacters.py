class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = res = 0
        for i in range(len(s)):
            if s[i] not in window:
                res = max(res,i-l+1)
            else:
                if window[s[i]] < l:
                    res = max(res,i-l+1)
                else:
                    l = window[s[i]] + 1
            window[s[i]] = i
        return res