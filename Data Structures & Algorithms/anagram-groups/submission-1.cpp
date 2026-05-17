#include<unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram_map;

        for (const auto& s : strs) {
            vector<int> string_char(26, 0);
            for (char c : s) {
                string_char[c - 'a']++;
            }

            string key = to_string(string_char[0]);
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(string_char[i]);
            }
            // cout << key;
            anagram_map[key].push_back(s);
        }
    
    vector<vector<string>> result;
    for (const auto& pair : anagram_map) {
        result.push_back(pair.second);
    }

    return result;
        
    }
};
