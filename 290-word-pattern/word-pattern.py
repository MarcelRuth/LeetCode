class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        mapping = {}
        if len(s) != len(pattern):
            return False
        for c, w in zip(pattern, s):
            if not c in mapping:
                if w in mapping.values():
                    return False
                mapping[c] = w
            if c in mapping:
                if mapping[c] != w:
                    return False
        return True