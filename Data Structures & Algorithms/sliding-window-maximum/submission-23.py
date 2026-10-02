from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        l = 0
        for r in range(0, len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()

            if r +1  >= k:
                res.append(nums[queue[0]])
                l += 1
        return res
            