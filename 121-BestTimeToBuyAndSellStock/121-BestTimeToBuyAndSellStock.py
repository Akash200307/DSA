# Last updated: 2/3/2026, 9:42:13 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1

        profits=0


        while j<len(prices):
            if prices[i]<prices[j]:
                profit=prices[j] - prices[i]
                profits=max(profit,profits)
            else:
                i=j
            j+=1

        return profits

