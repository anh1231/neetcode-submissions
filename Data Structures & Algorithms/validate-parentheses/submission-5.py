class Solution:
    def isValid(self, s: str) -> bool:
        correct = {']':'[', '}':'{', ')':'('}

        if (len(s) % 2) != 0:
            return False
        
        stored = []

        for c in s:
            if c in correct:
                if stored and stored[-1] == correct[c]:
                    stored.pop()
                else:
                    return False
            else:
                stored.append(c)
        return True if not stored else False