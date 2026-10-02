class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #use caching to store the max at each index for states buying and selling
        #dfs to find every solution
        cache = {} #key = (i, buying)

        def dfs(i, buying):
            #basecases
            #out of range
            if i >= len(prices):
                return 0
            #in cache
            if (i, buying) in cache:
                return cache[i,buying]
            

            #decisions: IF buying and IF selling
            if buying:
                #either buy or cooldown
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                #update cache
                cache[(i,buying)] = max(buy, cooldown)
            else:
                #either sell or cooldown
                #+2 to avoid cooldown day
                sell = dfs(i+2, not buying ) + prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i,buying)] = max(sell, cooldown)

            #return current state
            return cache[i,buying]

        
        #always buy at the start
        dfs(0, True)
        return cache[0,True]