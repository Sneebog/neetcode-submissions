class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two options 
        # buyinh or selling and cooldown
        cache = {} #(i, buying) = value

        def dfs(i, buying):
            #must sell at last point
            if i >= len(prices):
                return 0

            #use cache
            if (i, buying) in cache:
                return cache[(i,buying)]
            
            if buying:
                #buy or cooldown
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                choice = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                choice = max(sell, cooldown)
            
            cache[(i,buying)] = choice
            return choice
        
        return dfs(0, True)