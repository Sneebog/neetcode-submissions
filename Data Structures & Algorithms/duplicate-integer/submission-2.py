class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            val = num_dict.get(num)
            if val is None:
                num_dict[num] = True 
            else:
                return True
        return False 
