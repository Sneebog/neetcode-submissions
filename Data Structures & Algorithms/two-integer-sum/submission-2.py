class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i in range(0, len(nums)):
            nums_hash[nums[i]] = nums_hash.get(nums[i], [])
            nums_hash[nums[i]].append(i)

        
        for key in nums_hash:
            if target - key == key:
                if len(nums_hash.get(key)) >= 2:
                    return nums_hash.get(key)
            else:
                if nums_hash.get(target-key) is not None:
                    val1 = nums_hash.get(key)[0]
                    val2 = nums_hash.get(target-key)[0]
                    if val1 < val2:
                        return [val1,val2]
                    else:
                        return [val2,val1]
