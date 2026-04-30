class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == target:
                    return l
            elif nums[r] == target:
                    return r
            
            if nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
            else:
                return -1
        return -1