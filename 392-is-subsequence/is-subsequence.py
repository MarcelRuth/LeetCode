class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        next_index = 0
        was_found = False
        found_subs = 0
        for sub_s in s:
            for i in range(next_index, len(t)):
                if sub_s == t[i]:
                    next_index = i + 1
                    was_found = True
                    found_subs += 1
                    break
                else:
                    was_found = False
                    continue
            if not was_found:
                return False
        if found_subs == len(s):
            return True 
        else:
            return False