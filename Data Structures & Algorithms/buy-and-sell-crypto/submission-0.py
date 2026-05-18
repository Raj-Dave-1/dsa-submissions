class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxList = []
        l = len(prices)
        maxV = 0
        for i in range(l-1, -1, -1):
            maxList.insert(0, maxV)
            maxV = max(prices[i], maxV)
        
        ans = 0
        for i in range(l):
            ans = max(ans, maxList[i]-prices[i])

        return ans
