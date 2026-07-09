class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        numA = nums[1:]
        numB = nums[:len(nums)-1]
        #in place calculations
        return max(self.v1(numA), self.v1(numB))

    def v1(self, nums):
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums[0], nums[-1])
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            #last spot and this spot plus before
            nums[i] = max(nums[i-1], nums[i] + nums[i-2])
            print(nums)
        return nums[len(nums) -1]