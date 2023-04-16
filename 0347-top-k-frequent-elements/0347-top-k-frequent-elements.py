class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            numsDict[n] = 1 + numsDict.get(n, 0)
        for n, c in numsDict.items():
            # print([n,c])
            freq[c].append(n)
            
        # print(freq)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
        
            
#         for i in nums:
#             if numsDict.get(i, -1) == -1:
#                 numsDict[i] = 1
#             else:
#                 numsDict[i] += 1
#         while k != 0:
            
#             k -= 1
#         print(max(numsDict.values()))