class Solution {
public:
    int trap(vector<int>& height) {

        if (height.empty()) return 0;

        int l = 0, r = height.size() - 1;
        int maxLeft = height[l], maxRight = height[r];
        int maxArea = 0;

        while (l < r) {
            if (maxLeft < maxRight) {
                ++l;
                maxLeft = std::max(maxLeft, height[l]);
                maxArea += maxLeft - height[l];
            }
            else {
                --r;
                maxRight = std::max(maxRight, height[r]);
                maxArea += maxRight - height[r];
            }
        }

        return maxArea;

        
    }
};
