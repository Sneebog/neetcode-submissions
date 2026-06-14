class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        nums.sort()
        def dfs(i):
            res.add(tuple(subset))
            if i >= len(nums):
                return
            
            #backtracking 
            #either add pos I or don't 
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return [list(sub) for sub in res]

                