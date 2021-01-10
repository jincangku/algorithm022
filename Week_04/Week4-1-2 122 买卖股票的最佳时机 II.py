class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            return 0
        if prices[0] > prices[1]:
            start = 1
            buy = sell = prices[1]
        else:
            start = 0
            buy = sell = prices[0]

        for i in range(start + 1, len(prices)):
            if prices[i] > sell:
                max_profit += prices[i] - buy
                buy = sell = prices[i]
            else:
                buy = sell = prices[i]

        return max_profit
