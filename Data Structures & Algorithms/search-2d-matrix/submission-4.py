class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for m in matrix:
        #     l = 0
        #     r = len(matrix[0]) - 1

        #     while l <= r:
        #         i = (r + l) // 2
        #         if m[i] > target:
        #            r = i - 1
        #         elif m[i] < target:
        #             l = i + 1
        #         else:
        #             return True 

        # return False
        row = matrix[0]
        for m in matrix:
            if m[len(m)-1] >= target:
                row = m
                break

        l = 0
        r = len(row)-1
        while l <= r:
            i = (r+l)//2
            if row[i] > target:
                r = i - 1
            elif row[i] < target:
                l = i + 1
            else:
                return True

        return False

