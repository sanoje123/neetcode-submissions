class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ## O(n2) solution:
        # max_area = 0
        # for i in range(0, len(heights)):
        #     for j in range(i + 1, len(heights)):

        #         length = j - i
        #         min_hight = min(heights[i], heights[j])
        #         max_area = max(max_area, length * min_hight)
                
        # return max_area

        #O(n) solution
        max_area = 0

        start = 0
        end = len(heights) - 1
        while start < end:
            length = end - start
            min_hight = min(heights[start], heights[end])
            max_area = max(max_area, min_hight * length)

            if min(heights[start], heights[end]) == heights[start]:
                start += 1
            else: end -= 1

        return max_area





                
        