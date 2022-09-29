class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Trivial solution below, 33ms runtime:
        """
        return s.lower()
        
        """
        My attempt at a solution without using built-in features,
        but way too slow compared to above^ (64 ms runtime)
        """
        # if len(s) == 0:
        #     return s
        # output = ''
        # for i in range(0, len(s)):
        #     if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        #         output += chr(ord(s[i]) + 32)
        #     else:
        #         output += s[i]
        # return output