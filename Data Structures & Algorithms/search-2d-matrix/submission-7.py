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


        # row = matrix[0]
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (bot + top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        row = (bot + top) // 2
        l = 0
        r = len(matrix[row])-1
        while l <= r:
            i = (r+l)//2
            if matrix[row][i] > target:
                r = i - 1
            elif matrix[row][i] < target:
                l = i + 1
            else:
                return True

        return False

