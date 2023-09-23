class Solution:
    def myPow(self, x: float, n: int) -> float:
        # divide the work using binary representation of exponents

        # invert as x^-1 = 1/x ...
        if  n < 0:
            n = -n
            x = 1 / x

        res = 1
        
        while n != 0:
            if (n % 2) != 0:
                res *= x
            
            x *= x
            n = n // 2

        return res
