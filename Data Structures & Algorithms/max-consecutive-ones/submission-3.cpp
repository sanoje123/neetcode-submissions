class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curr_len = 0, max_len = 0;
        for (int num : nums) {
            if (num == 1) {
                curr_len += 1;
            } else {
                max_len = max(max_len, curr_len);
                curr_len = 0;
            }
        }
        max_len = max(max_len, curr_len);

        return max_len;
    }
};