class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for string in strs:
            count = [0] * 26
            
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            if wordDict.get(tuple(count), -1) == -1:
                wordDict[tuple(count)] = [string]
            else:
                wordDict[tuple(count)].append(string)
        
        
        
        
#         for string in strs:
#             letterDict = {}
#             for letter in string:
#                 if letterDict.get(letter, 0) == 0:
#                     letterDict[letter] = 1
#                 else:
#                     letterDict[letter] += 1        
                    
#             letterTuple = tuple(letterDict)
#             wordDict[letterTuple].append(string)

            
        return wordDict.values()