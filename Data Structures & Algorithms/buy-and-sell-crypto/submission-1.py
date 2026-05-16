class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0
        max_prices = [0] * l
        min_prices = [0] * l
        
        min_prices[0], max_prices[l -1] = prices[0], prices[l- 1]


        #one for loop
        max_count = l -2   
        for i in range(1, l):
            if prices[i] < min_prices[i -1]:
                min_prices[i] = prices[i]
            else:
                min_prices[i] = min_prices[i -1 ]
            
            if prices[max_count] > max_prices[max_count + 1]:
                max_prices[max_count] = prices[max_count]
            else:
                max_prices[max_count] = max_prices[max_count+ 1 ]
            max_count -= 1

        #profit calculation
        max_profit = 0
        for i in range(0, l):
            profit = max_prices[i] - min_prices[i]
            max_profit = max(max_profit, profit)
        
        return max_profit