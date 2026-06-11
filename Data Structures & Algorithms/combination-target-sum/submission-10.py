class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #gonna use same approach as before with more restrictions on sum amount 
        res = []
        subset = []

        def dfs(i,sub_sum):
            if sub_sum == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or sub_sum >= target:
                return
            val = nums[i]
            subset.append(val)
            #two options 
            #1. add itself again
            dfs(i, sub_sum + val)
            #2. add next val
            subset.pop()
            dfs(i+1, sub_sum)

        dfs(0, 0)
        return res
