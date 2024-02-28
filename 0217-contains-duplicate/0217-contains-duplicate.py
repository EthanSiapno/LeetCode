class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if numsDict.get(num, 0) == 0:
                numsDict[num] = 1
            else:
                return True
                numsDict[num] += 1
        return False