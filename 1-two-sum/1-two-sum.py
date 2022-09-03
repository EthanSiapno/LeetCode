class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            val = target - nums[i]
            if val in nums[i+1:]:
                return [i, nums.index(val, i+1)]
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if i != j and nums[i]+nums[j] == target:
        #             return [i, j]