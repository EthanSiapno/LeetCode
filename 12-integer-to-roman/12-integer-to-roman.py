class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num = ''
        new_num = str(num)
        for i in range(0, len(new_num)):
            roman_num += self.roman2_helper(int(new_num[i]), len(new_num[i+1:]))
        return roman_num
        
    def roman2_helper(self, digit, rl):
        """
        rl represent remaining_length of the string/number.
        Precondition: Since intToRoman2 only works for values between [1, 3999]
        inclusive, variable rl can only be <= 3. Therefore, if rl = 3, only
        one digit will be inputted into the digit_helper function.
        """
        if rl == 3:
            return self.digit_helper(digit, 'M', '', '')
        if rl == 2:
            return self.digit_helper(digit, 'C', 'D', 'M')
        if rl == 1:
            return self.digit_helper(digit, 'X', 'L', 'C')
        if rl == 0:
            return self.digit_helper(digit, 'I', 'V', 'X')
        
        return
    
    def digit_helper(self, digit, letter1, letter2, letter3):
        """
        Helps construct a roman equivalent of a given digit.
        Precondition: Since intToRoman2 only works for values between [1, 3999]
        inclusive, variable rl can only be <= 3.
        """
        letter = ''
        if digit == 9:
            letter += letter1 + letter3
            return letter
        if digit == 4:
            letter += letter1 + letter2
            return letter
        while(digit > 4):
            letter += letter2
            digit -= 5
        while(digit > 0):
            letter += letter1
            digit -= 1
        return letter