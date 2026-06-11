class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #gonna use same approach as before with more restrictions on sum amount 
        res = []
        hash_map = {}
        subset = []
        #sub_sum = 0

        def dfs(i,sub_sum):
            if sub_sum == target:
                res.append(subset.copy())

            if i >= len(nums) or sub_sum >= target:
                return
            val = nums[i]
            subset.append(val)
            sub_sum = sub_sum + val
            #three options 
            #1. add itself again
            dfs(i, sub_sum)
            #2. add next val
            dfs(i+1, sub_sum)
            #3. don't add either
            subset.pop()
            sub_sum = sub_sum - val
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
