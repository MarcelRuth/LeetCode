class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n_length = len(needle)
        if len(haystack) == 1:
            if needle == haystack:
                return 0
            else:
                return -1

        for i in range(0, len(haystack) - n_length + 1):
            if needle == haystack[i:i + n_length]:
                return i
        return -1