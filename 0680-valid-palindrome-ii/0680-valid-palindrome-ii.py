class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                if l == 0:
                    return s[l:r] == s[r-1::-1] or s[l+1:r+1] == s[r:l:-1]
                else:
                    return s[l+1:r+1] == s[r:l:-1] or s[l:r] == s[r-1:l-1:-1]
                    
            l += 1
            r -= 1
        return True