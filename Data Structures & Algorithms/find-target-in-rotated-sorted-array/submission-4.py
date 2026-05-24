class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        l = 0 
        r = len(nums) -1
        min_pos = 0
        while l <= r:
            if nums[l] < nums[r]:
                if nums[min_pos] > nums[l]:
                    min_pos = l 
                break 

            m = (l + r ) // 2
            if nums[min_pos] > nums[m]:
                min_pos = m 
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        
        if min_pos == 0:
            l = 0
            r = len(nums) - 1
        elif target >= nums[0]:
            l = 0
            r = min_pos - 1
        else:
            l = min_pos
            r = len(nums) - 1


        while l <= r:
            m = (l + r ) // 2
            print(m, l, r)
            if nums[m] == target:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1

    
            
            

