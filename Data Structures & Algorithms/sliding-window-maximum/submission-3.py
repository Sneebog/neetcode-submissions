from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        max_arr = []
        queue = deque()
        for r in range(0,len(nums)):
            queue.append(nums[r])
            # print(queue, r, l)
            # print(max_arr)
            if r - l  + 1>= k:
                window_max = max(queue)
                max_arr.append(window_max)
            while r - l  + 1>= k:
                queue.popleft()
                l += 1
         
        return max_arr
            