class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1
        for i in new_nums:
            count = 1
            while i+1 in new_nums:
                count += 1
                i += 1
            longest = max(longest, count)
        return longest
