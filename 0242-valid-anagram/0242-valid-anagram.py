class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        
        if len(s) != len(t):
            return False
        
        for letter in s:
            if sDict.get(letter) == None:
                sDict[letter] = 1
            else:
                sDict[letter] += 1

        for letter in t:
            if sDict.get(letter) == None:
                return False
            if tDict.get(letter) == None:
                tDict[letter] = 1
            else:
                tDict[letter] += 1
        
        for key in sDict:
            if sDict[key] != tDict[key]:
                return False
            
        return True
        