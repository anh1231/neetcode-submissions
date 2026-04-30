class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-l)//2)
            
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            if nums[r] < target:
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m
            elif nums[r] > target:
                if nums[m] == target:
                    return m
                elif nums[m] > target and nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
        return -1