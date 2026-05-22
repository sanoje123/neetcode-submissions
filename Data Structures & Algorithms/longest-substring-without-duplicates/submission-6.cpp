class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        // // O(n2)
        // unordered_set<char> set_c;
        // int max_len = 0;

        // for (int i = 0; i < s.size(); ++i) {
        //     set_c.clear();
        //     int help = 0;
        //     for (int j = i; j < s.size(); ++j) {
        //         if (set_c.count(s[j])) break;
        //         set_c.insert(s[j]);
        //         help++;

        //     }
        //     max_len = max(max_len, help);
        // }
        // return max_len;


        // O(n)
        unordered_set<char> set_c;
        int l = 0, max_s = 0, r = 0;

        while (r < s.size()) {
            while (set_c.count(s[r]))  {
                set_c.erase(s[l]);
                l++;
            };
            set_c.insert(s[r]);
            r++;
            max_s = max(max_s, r - l);
        }

        return max_s;

    }
};
