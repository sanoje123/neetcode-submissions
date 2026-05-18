#include<unordered_set>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set_nums(nums.begin(),nums.end());

        int max_len = 0;
        for (int num : set_nums) {
            if (!set_nums.count(num - 1)) {
                int help_set = 1;
                while (set_nums.count(num + 1)) {
                    ++help_set;
                    ++num;
                }
                max_len = max(help_set, max_len);
            }
        }
        return max_len;
    }
};
