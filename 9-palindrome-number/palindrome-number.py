class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)
        
        if len(x) == 1:
            return True

        for i in range(len(x)):
            if i < len(x)/2:
                if x[i] == x[-(i+1)]:
                    continue
                else:
                    return False
            else:
                return True