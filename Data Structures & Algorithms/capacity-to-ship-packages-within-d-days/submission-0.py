class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            cap = l + (r-l) // 2
            count = 1
            acc = 0
            for w in weights:
                if acc + w <= cap:
                    acc += w
                else:
                    acc = w
                    count += 1
            if count > days:
                l = cap + 1
            else:
                res = min(res, cap)
                r = cap - 1
        return res


