class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.lower()
        check = []
        for i in res:
            if i.isalnum():
                check.append(i)
        return check == check[::-1]