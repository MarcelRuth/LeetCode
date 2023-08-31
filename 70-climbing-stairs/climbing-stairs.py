class Solution:
    def climbStairs(self, n: int) -> int:
        # like Fibonacci Computation
        previous = 1
        current = 1
        for i in range(2, n + 1):
            next = current + previous
            previous, current = current, next
        return current
