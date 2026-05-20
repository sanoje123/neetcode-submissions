class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        max_area = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                max_area += maxLeft - height[l]
            
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                max_area += maxRight - height[r]


        return max_area        