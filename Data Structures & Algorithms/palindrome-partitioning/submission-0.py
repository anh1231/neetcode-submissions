class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        tmp = []

        def dfs(i):
            if i == len(s):
                res.append(tmp.copy())
            
            for j in range(i, len(s)):
                part = s[i:j+1]

                if self.isPalindrome(part):
                    tmp.append(part)
                    dfs(j+1)
                    tmp.pop()
        dfs(0)
        return res



    def isPalindrome(self,s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True