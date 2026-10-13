from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        for r in range(0, len(nums)):
            #add r to list
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r) 

            #if front isn't in window
            if q[0] < l:
                q.popleft()
            
            #if window is valid
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res