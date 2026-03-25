from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit"""
        buyingprice = prices[0]
        profit = 0
        for i in range(1,len{prices}):
        sellingPrice = price[i]
        if sellingPrice > buyingprice:
            profit = max(profit,sellingPrice - buyingprice)
        if buyingprice =sellingPrice()
        buyingprice = sellingPrice  
        return profit  

