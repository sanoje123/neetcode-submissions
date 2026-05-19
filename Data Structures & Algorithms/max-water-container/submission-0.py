class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(0, len(heights)):
            for j in range(i + 1, len(heights)):

                length = j - i
                min_hight = min(heights[i], heights[j])
                max_area = max(max_area, length * min_hight)
                
        return max_area
                
        