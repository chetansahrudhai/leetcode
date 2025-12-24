class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        space = sum(capacity)
        apples = sum(apple)
        if space < apples:
            return 0
        for i in range(0, len(capacity)):
            if capacity[i] > apples:
                return i+1
            else:
                apples -= capacity[i]
                if apples == 0:
                    return i+1
        return len(capacity)