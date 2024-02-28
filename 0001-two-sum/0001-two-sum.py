class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            if numDict.get(target - nums[i],-1) == -1:
                numDict[nums[i]] = i
            else:
                return [numDict.get(target - nums[i]), i]