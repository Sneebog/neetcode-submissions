class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        calc_nums = [0]* len(nums)
        sum_val = 1 
        zero_num = 0 
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_num += 1
                pos = i
            else:
                sum_val = sum_val * nums[i]
        
        if zero_num > 1:
            return calc_nums
        elif zero_num == 1:
            calc_nums[pos] = sum_val
            return calc_nums
        else:
            for i in range(0, len(nums)):
                calc_nums[i] = int(sum_val / nums[i])
            return calc_nums
