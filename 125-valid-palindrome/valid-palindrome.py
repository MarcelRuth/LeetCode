class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(' ', '').lower()
        s = ''.join(filter(str.isalnum, s))
        for i in range(len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True
