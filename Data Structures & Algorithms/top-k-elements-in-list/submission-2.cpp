class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequncy_map; // number, fequency
        for (int n : nums){
            frequncy_map[n] = 1 + frequncy_map[n];
        }

        vector<vector<int>> frequncy_array(nums.size() + 1); // frequency, numbers

        for (const auto& item : frequncy_map){
            frequncy_array[item.second].push_back(item.first);
        }

        vector<int> res;
        for (int i = frequncy_array.size() - 1; i < 0; --i) {
            for (int n : frequncy_array[i]) {
                res.push_back(n);
                if (res.size() == k) return res;
            }
        }
    }
};
