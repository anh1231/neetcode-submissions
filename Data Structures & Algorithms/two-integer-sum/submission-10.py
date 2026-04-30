class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i,num in enumerate(nums):
            needed_num = target - num
            if needed_num in seen_nums:
                return [seen_nums[needed_num], i]
            seen_nums[num] = i