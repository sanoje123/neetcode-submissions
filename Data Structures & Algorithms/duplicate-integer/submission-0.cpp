#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> elements(nums.begin(), nums.end());
        return (nums.size() == elements.size()) ? false : true;
    }
};