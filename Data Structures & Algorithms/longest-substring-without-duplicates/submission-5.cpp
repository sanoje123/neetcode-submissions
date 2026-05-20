class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> set_c;
        int max_len = 0;

        for (int i = 0; i < s.size(); ++i) {
            set_c.clear();
            int help = 0;
            for (int j = i; j < s.size(); ++j) {
                if (set_c.count(s[j])) break;
                set_c.insert(s[j]);
                help++;

            }
            max_len = max(max_len, help);
        }
        return max_len;
    }
};
