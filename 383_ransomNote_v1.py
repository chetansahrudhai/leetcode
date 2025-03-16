class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount = {}
        for i in magazine:
            magazineCount[i] = magazineCount.get(i, 0) + 1
        for i in ransomNote:
            if magazineCount.get(i, 0) == 0:
                return False
            magazineCount[i] -= 1
        return True