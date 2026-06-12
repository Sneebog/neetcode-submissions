class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        subset = []
        candidates.sort()
        def dfs(i, sub_sum):
            if sub_sum == target:
                res.add(tuple(subset))
                return 

            if sub_sum > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+ 1, sub_sum + candidates[i])
            
            subset.pop()
            j = i
            while candidates[i] == candidates[j]:
                j += 1
                if j >= len(candidates):
                    return
            dfs(j, sub_sum)
        dfs(0, 0)
        return [list(combination) for combination in res]