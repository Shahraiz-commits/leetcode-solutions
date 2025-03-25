class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left and right pointer. Use greedy to determine optimal choice
        maxProfit=0

        while(r!=len(prices)):
            if(prices[l] < prices[r]):
                diff = prices[r] - prices[l]
                maxProfit = max(diff, maxProfit)         
            else:
                l = r
            r+=1
        return maxProfit

