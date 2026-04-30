class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in seen_nums:
                return [seen_nums[needed_num], i]
            seen_nums[nums[i]] = i