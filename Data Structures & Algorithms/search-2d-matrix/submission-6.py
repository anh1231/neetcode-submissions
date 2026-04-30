class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i,row in enumerate(matrix):
            if row[-1] >= target:
                for num in matrix[i]:
                    if num <= target:
                        if num == target:
                            return True
                    else:
                        break
                break
        return False
            