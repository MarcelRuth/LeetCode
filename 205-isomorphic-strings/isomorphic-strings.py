class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for i, j in zip(s, t):
            if i not in mapping:
                # No two characters may map to the same character,
                # but a character may map to itself.
                if j not in mapping.values():
                    mapping[i] = j
                else:
                    return False
            else:
                if mapping[i] == j:
                    continue
                else:
                    return False
        return True