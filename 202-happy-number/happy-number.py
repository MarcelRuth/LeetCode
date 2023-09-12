class Solution:
    def isHappy(self, n: int) -> bool:

        was_there = set()

        def square(n):
            if n in was_there:
                return False

            was_there.add(n)
            s = sum(int(d) ** 2 for d in str(n))

            if s == 1:
                return True
                
            return square(s)

        return square(n)