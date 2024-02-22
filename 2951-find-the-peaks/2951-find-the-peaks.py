class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        output = []
        for i in range(len(mountain)-1):
            if i != 0 and i != len(mountain) - 1:
                # print(i + 100)
                if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                    # print(i + 200)
                    output.append(i)
        
        return output