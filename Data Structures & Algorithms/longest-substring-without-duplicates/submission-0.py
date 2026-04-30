class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        res = 0
        l, r = 0,0

        while r < len(s):
            while s[r] in longest:
                longest.remove(s[l])
                l += 1
            longest.add(s[r])
            res = max(len(longest), res)
            r += 1
        return res