class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 1
        for i in nums:
            count = 1
            while i+1 in nums:
                count += 1
                longest = max(longest, count)
                i += 1
        return longest
