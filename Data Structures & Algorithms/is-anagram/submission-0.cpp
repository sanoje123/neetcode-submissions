#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(const string& s, const string& t) {

        if (s.size() != t.size()) return false;

        unordered_map<char, int> anagram_map;

        for (char cs : s) {
            anagram_map[cs]++;
        }

        for(char ct : t) {
            anagram_map[ct]--;
        }
        
        for (auto pair : anagram_map) {
            if (pair.second != 0) return false;
        }

        return true;
    }
};
