class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        int end = numbers.size() - 1;

        while (start < end) {
            int sum_br = numbers[start] + numbers[end];

            if (sum_br > target) end--;
            else if (sum_br < target) start++;
            else return {start + 1, end + 1};
        }
        return {};
        
    }
};
