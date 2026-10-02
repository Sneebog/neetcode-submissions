class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #same but sell as many times?
        res = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res += prices[r] - prices[l]
                l = r
            else:
                l = r
            r +=1
        return res
