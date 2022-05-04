class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Approach 1
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        #Len = len(prices)
        #if Len == 1: return 0
        #diff = 0
        #small, large = prices[0], prices[0]
        #for i in range(1, Len):
        #    if large < prices[i]:
        #        large = prices[i]
        #    if small > prices[i]:
        #        small = prices[i]
        #        large = prices[i]
        #    if diff < large - small:
        #        diff = large - small
        #return diff
    
        ## Approach 2
        ## Time complexity: O(N)
        ## Space complexity: O(1)
        Len = len(prices)
        if Len == 1: return 0
        cur, diff = prices[0], 0
        for i in range(1, Len):
            cur = min(cur, prices[i])
            diff = max(diff, prices[i] - cur)
        return diff
        
