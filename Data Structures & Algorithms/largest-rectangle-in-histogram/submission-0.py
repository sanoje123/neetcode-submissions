class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_h = 0

        for i, h in enumerate(heights):
            if stack and stack[-1][1] > h:
                start_index = -1
                while stack and stack[-1][1] > h:
                    element = stack.pop()
                    start_index = element[0]
                    height = element[1]
                    max_h = max(max_h, height*(i - start_index))
                stack.append((start_index, h))

            else:
                stack.append((i, h))

        while stack:
            element = stack.pop()
            start_index = element[0]
            height = element[1]
            max_h = max(max_h, height*(len(heights) - start_index))

        return max_h