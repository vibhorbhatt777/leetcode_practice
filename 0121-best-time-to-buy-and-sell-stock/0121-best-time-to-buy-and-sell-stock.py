class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """ it is brute force approach - give TLE(time limit exceeded)
        n = len(prices)
        max_profit = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if prices[j]> prices[i]:
                    p = prices[j] - prices[i]
                    max_profit = max(max_profit,p)

        """
        n = len(prices)
        max_profit = 0
        min_price = float("inf")
        for i in range(0,n):
            min_price = min(min_price , prices[i])
            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit

        