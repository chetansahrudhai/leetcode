class Solution:
    def countCollisions(self, directions: str) -> int:
        return sum(i!='S' for i in directions.rstrip('R').lstrip('L'))