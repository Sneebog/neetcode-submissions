class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = l + (r-l) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            if count > h:
                l = k + 1
            else:
                res = min(res, k) 
                r = k - 1
        return res

