class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        res = 0

        for i in prices:
            lowest = min(lowest, i)
            res = max(res,i - lowest)
        return res