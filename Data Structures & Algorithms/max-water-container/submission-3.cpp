#include<algorithm>

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;

        int start = 0;
        int end = heights.size() - 1;

        while (start < end) {
            int length = end - start;
            int area = std::min(heights[start], heights[end]) * length;
            max_area = std::max(max_area, area);

            if (heights[start] <= heights[end]) {
                ++start;
            } else {
                --end;
            }
        }
        return max_area;
        
    }
};
