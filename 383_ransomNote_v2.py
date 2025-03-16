class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for char in set(ransomNote):
            M = magazine.count(char)
            R = ransomNote.count(char)
            if R > M:
                return False
        return True