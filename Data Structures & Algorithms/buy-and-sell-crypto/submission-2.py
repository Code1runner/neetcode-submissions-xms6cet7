class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for buy_index in range(len(prices)):
            for sell_index in range(buy_index+1, len(prices)):
                res = max(res, prices[sell_index] - prices[buy_index])
        return res