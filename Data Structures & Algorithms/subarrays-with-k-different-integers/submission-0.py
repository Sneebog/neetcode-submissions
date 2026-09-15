class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def at_most(k):
            if k < 0:
                return 0
            freq = {}
            left = 0
            distinct = 0
            count = 0

            for right in range(0, len(nums)):
                x = nums[right]
                if freq.get(x,0) == 0:
                    distinct += 1
                freq[x] = freq.get(x,0) + 1

                while distinct > k:
                    y = nums[left]
                    freq[y] -= 1
                    if freq[y] == 0:
                        distinct -= 1
                    left += 1

                count += right -left + 1
            return count
        return at_most(k) - at_most(k - 1)