class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0
        for num in nums:
            streak = 0
            if num - 1 not in num_set:
                streak = 1
                while num + streak in num_set:
                    streak += 1
                max_sequence = max(max_sequence, streak)
        return max_sequence