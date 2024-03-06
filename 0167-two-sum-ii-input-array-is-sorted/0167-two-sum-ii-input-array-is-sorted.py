class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        
        while index1 < len(numbers):
            if target - numbers[index1] in numbers[index1+1:]:
                index2 = index1 + 1
                while index2 < len(numbers):
                    if target - numbers[index1] == numbers[index2]:
                        return [index1+1, index2+1]
                    else:
                        index2 += 1
            else:
                index1 += 1
            
        
        return [-1]