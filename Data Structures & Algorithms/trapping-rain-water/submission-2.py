class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax =[0] * len(height)
        rightmax = [0] * len(height)
        leftmax[0] = height[0]
        rightmax[len(height) -1] = height[len(height) - 1]
        for i in range(0, len(height)):
            if height[i] > leftmax[i - 1]:
                leftmax[i] = height[i]
            else:
                leftmax[i]= leftmax[i -1]
        
        for j in range(len(height) - 2, -1, -1):
            if height[j] > rightmax[j + 1]:
                rightmax[j] = height[j]
            else:
                rightmax[j]= rightmax[j + 1]
        vol = 0

        for k in range(1, len(height) -1):
            vol += min(leftmax[k], rightmax[k]) - height[k]
        
        return vol