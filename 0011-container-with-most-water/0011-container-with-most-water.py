class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum = 0
        temp = 0
        
        while l < r:
            temp = (r - l) * (min(height[l], height[r]))
            if temp > maximum:
                maximum = temp
            else:
                if height[l] > height[r]:
                    r -= 1
                else:
                    l += 1
        
        return maximum