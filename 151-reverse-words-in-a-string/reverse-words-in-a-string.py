class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        output = ''
        for i in range(len(s) -1, -1, -1):
            if not ' ' in s[i] and len(s[i]) > 0:
                output += s[i] + ' '
        return output.strip()