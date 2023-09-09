class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for i, j in zip(s, t):
            if i not in mapping:
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