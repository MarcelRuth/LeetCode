class Solution:
    def mySqrt(self, x: int) -> int:
        square = 0
        counter = 1
        while square <= x:
            square = counter * counter
            counter += 1
        
        return counter - 2