class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #gonna use same approach as before with more restrictions on sum amount 
        res = []
        subset = []
        #sub_sum = 0

        def dfs(i,sub_sum):
            if sub_sum == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or sub_sum >= target:
                return
            val = nums[i]
            subset.append(val)
            #three options 
            #1. add itself again
            dfs(i, sub_sum + val)
            #2. add next val
            dfs(i+1, sub_sum + val)
            #3. don't add either
            subset.pop()
            dfs(i+1, sub_sum)

        dfs(0, 0)
        if not(res):
            return []
        res.sort()
        out = [res[0]]
        for i in range(1, len(res)):
            if res[i] != res[i-1]:
                out.append(res[i])
        return out
