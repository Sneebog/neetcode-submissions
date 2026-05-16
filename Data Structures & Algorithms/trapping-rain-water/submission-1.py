class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        hash_map = {}
        while left < right:
            h = min(height[left], height[right])
            for i in range(left, right):
                vol = h - height[i]
                hash_map[i] = max(vol, hash_map.get(i, 0))
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1

        total_vol= 0
        for val in hash_map.values():
            total_vol += val
        
        return total_vol