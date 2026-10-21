class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        min_p = prices[0]
        max_p = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
                max_p = prices[i]
            else:
                max_p = max(max_p, prices[i])
                res = max(max_p - min_p, res)
        return res