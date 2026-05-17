class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = height[0]
        maxR = height[n -1]
        l, r = 0, n - 1
        vol = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                vol += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                vol += maxR - height[r]
        
        return vol

            

