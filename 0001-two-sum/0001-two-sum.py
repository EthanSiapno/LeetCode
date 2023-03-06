class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if nums_dict.get(nums[i], -1) == -1:
                nums_dict[key] = i
            else:
                return [nums_dict[nums[i]], i]

            
