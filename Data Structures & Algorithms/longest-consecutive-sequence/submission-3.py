class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hashmap = {}
        max_sequence = 0
        
        for i in range(0, len(nums)):
            if num_hashmap.get(nums[i] - 1) is not None:
                num_hashmap[nums[i]-1] = nums[i]

            if num_hashmap.get(nums[i] + 1) is not None:
                num_hashmap[nums[i]] = nums[i] + 1
            else:
                num_hashmap[nums[i]] = -1

        loop_count = 0
        sequence_count = 0
        while loop_count < len(nums):
            if num_hashmap.get(nums[loop_count] + sequence_count) is not None:
                sequence_count += 1
            else:
                if sequence_count > max_sequence:
                    max_sequence = sequence_count
                sequence_count = 0
                loop_count += 1
        
        return max_sequence


            

