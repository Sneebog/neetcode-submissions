class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #outer loop 
        #needs to be -2 to ensure there is 3
        nums.sort()
        for i in range(0, len(nums) -2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1 
        
            while l < r:
                if -nums[i] == nums[r] + nums[l]:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l -1 ]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1 ]:
                        r -= 1
                
                elif -nums[i] < nums[r] + nums[l]:
                    r -= 1
                else:
                    l += 1
        return res