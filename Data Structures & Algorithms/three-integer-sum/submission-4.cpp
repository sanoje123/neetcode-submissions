#include<vector>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> out;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int start = i + 1, end = nums.size() - 1;
            int target_sum = 0 - nums[i];
            while (start < end) {
                if (nums[start] + nums[end] < target_sum) ++start;
                else if (nums[start] + nums[end] > target_sum) --end;
                else {
                    out.push_back({nums[i], nums[start], nums[end]});
                    ++start;
                    while ((nums[start] == nums[start - 1]) && start < end) ++start;
                }
            }
        }

        return out;
        
    }
};
