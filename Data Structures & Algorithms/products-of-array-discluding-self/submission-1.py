class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        output = [0] * len(nums)
        roll_val = 1
        for i in range(0 , len(nums)):
            roll_val = roll_val * nums[i]
            prefix[i] = roll_val
        print(prefix)
        roll_val = 1
        for i in range(len(nums) -1,-1, -1):
            roll_val = roll_val * nums[i]
            suffix[i] = roll_val
        print(suffix)
        for i in range(0, len(nums)):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(nums) -1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]
        
        return output
