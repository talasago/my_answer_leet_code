class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
            else:
                profit = profit if profit > price - min_price else price - min_price

        return profit 
