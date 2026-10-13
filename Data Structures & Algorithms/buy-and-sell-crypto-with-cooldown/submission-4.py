class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #tree
        #two options of buy or sell
        # and cooldown
        #use a cache
        cache = {} #(i, buying) : value
        def dfs(i, buying):
            if i > len(prices) - 1:
                return 0

            if (i, buying) in cache:
                return cache[(i,buying)]

            #two options
            if buying:
                #buy option
                buy = dfs(i+1, not(buying)) - prices[i]
                cooldown = dfs(i+1, buying)
                out = max(buy, cooldown)
            else:
                #sell option
                sell = dfs(i+2, not(buying)) + prices[i]
                cooldown = dfs(i+1, buying)
                out = max(sell, cooldown)
            
            cache[(i,buying)] = out
            return out 


        return dfs(0, True)