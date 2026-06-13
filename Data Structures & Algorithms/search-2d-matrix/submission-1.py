class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            l = 0
            r = len(matrix[0]) - 1

            while l <= r:
                i = (r + l) // 2
                if m[i] > target:
                   r = i - 1
                elif m[i] < target:
                    l = i + 1
                else:
                    return True 

        return False