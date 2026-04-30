class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        high = 0
        res = [0] * len(temperatures)
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                pop = stack.pop()
                res[pop[0]] = i - pop[0]
            stack.append((i,t))
        return res