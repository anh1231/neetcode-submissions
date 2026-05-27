class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_let = {2:['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4:['g', 'h', 'i']\
                    , 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's']\
                    , 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']
        }

        res = []
        total = 0
        for i in digits:
            if i in [7,9]:
                total += 4
            else:
                total += 3
        def dfs(i, cur):
            if i >= len(digits):
                if cur:
                    res.append(''.join(cur.copy()))
                return
            
            for j in num_let[int(digits[i])]:
                cur.append(j)
                dfs(i+1, cur)
                cur.pop()
        dfs(0, [])
        return res