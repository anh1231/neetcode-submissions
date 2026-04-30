class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        res = 0

        for i in prices:
            res = max(res,i - lowest)
            lowest = min(lowest, i)
        return res