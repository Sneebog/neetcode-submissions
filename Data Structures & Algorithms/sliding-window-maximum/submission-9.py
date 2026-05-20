class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []
        l = 0 

        for r in range(0, len(nums)):
            #pop smaller vaues from q
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if r + l + 1>= k:
                output.append(nums[queue[0]])
                l += 1

        return output 

