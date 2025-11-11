class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = [""]
        for digit in digits:
            digit = int(digit)
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for letter in options[digit]:
                    queue.append(curr + letter)
        return queue