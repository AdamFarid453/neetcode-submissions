class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 1
        while j < len(prices):
            # make sure price is always less
            print(i,j, max_profit)
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j]- prices[i])
            else:
                i=j
            j+=1
        return max_profit


