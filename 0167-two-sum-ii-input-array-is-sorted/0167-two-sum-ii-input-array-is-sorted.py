class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1
        # while numbers[index2] > target:
        #     index2 -= 1
        while numbers[index1] + numbers[index2] != target:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                return [index1+1, index2+1]
            
        
        return [index1+1, index2+1]