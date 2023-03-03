class Solution:
    def isValid(self, s: str) -> bool:
        left = '({['
        curr = ''
        for i in range(len(s)):
            if s[i] in left:
                curr += s[i]
            else:
                if len(curr) == 0:
                    return False
                if curr[-1] == '(' and s[i] != ')':
                    return False
                elif curr[-1] == '{' and s[i] != '}':
                    return False
                elif curr[-1] == '[' and s[i] != ']':
                    return False
                else:
                    curr = curr[:-1]
        if curr != '':
            return False
        return True