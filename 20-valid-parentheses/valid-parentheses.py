from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        open_brackets = deque()
        for c in s:
            if c in ['(', '{', '[']:
                open_brackets.append(c)
            else:
                if len(open_brackets) != 0:
                    if open_brackets.pop() == par_map[c]:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(open_brackets) == 0:
            return True
        else:
            return False
           

