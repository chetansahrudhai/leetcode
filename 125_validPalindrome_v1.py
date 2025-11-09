class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for i in s:
            if i.isalpha() == True or i.isdigit() == True:
                i = i.lower()
                check.append(i)
        if check == check[::-1]:
            return True
        else:
            return False