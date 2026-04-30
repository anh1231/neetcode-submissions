class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(stripped) - 1

        for i in range(len(stripped)//2):
            if stripped[left] != stripped[right]:
                return False
            left +=1
            right -=1
        return True