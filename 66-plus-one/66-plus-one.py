class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_d = ''
        for num in digits:
            str_d += str(num)
        
        str_d = int(str_d)
        str_d += 1
        
        str_d = str(str_d)
        
        output = []
        for i in str_d:
            output.append(int(i))
        return output
#         if digits[-1] != 9:
#             digits[-1] += 1
#         else:
#             digits[-1] = 0
#             digits[-2] += 1
            
#             fo
            
#             plusOne(digits[0:[-1]])
        
        
#         return digits
#         # digits
#         # print(digits[-1])
#         while (done = false):
#             for i in range(1, len(digits)):
#                 if digits[-i] == 9:
#                     digits[-i] = 
            
#         # if digits[-1] == 9:
        #     digits[-1] = 0
        #     digits[-2] = digits[-2] + 1
        # else:
        #     digits[-1] += digits[-1] + 1
        