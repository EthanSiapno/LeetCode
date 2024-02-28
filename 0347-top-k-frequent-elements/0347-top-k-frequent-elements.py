class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for key, val, in count.items() :
            frequency[val].append(key)
        
        output = []
        
        for i in range(len(frequency)-1, 0, -1):
	        for n in frequency[i]:
		        output.append(n)
		        if k == len(output):
			        return output
            
        
        
#         countDict = {}
#         countList = []
#         outputList = []
#         highestKey = 0
#         highestVal = 0
        
#         for num in nums:
#             if countDict.get(num,0) == 0:
#                 countDict[num] = 1
#             else:
#                 countDict[num] += 1
        
#         for key in countDict:
#             countList.append(tuple([key, countDict[key]]))
        
#         # print(countList)
        
#         while k > 0:
#             for pair in countList:
#                 if pair[1] > highestVal:
#                     if pair[0] not in outputList:
#                         highestVal = pair[1]
#                         highestKey = pair[0]
                
#             outputList.append(highestKey)
#             highestKey = 0
#             highestVal = 0
#             k -= 1
        
#         return outputList