class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        range_end = round(len(x_str) / 2)
        for i in range(range_end):
            if x_str[i] != x_str[-(i+1)]:
                return False
        return True