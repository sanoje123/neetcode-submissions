class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int len = 0;
        int help = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                help += 1;
            } else {
                if (help > len) {
                    len = help;
                };
                help = 0;
            }
        }
        if (help > len) {
            len = help;
        }
        
        return len;
    }
};