class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for i in nums:
            if numsDict.get(i) != None:
                return True
            else:
                numsDict[i] = i
        return False