#include<cctype>

class Solution {
public:
    bool isAlNum(char c) {
        return ('a' <= c && c <= 'z') ||
               ('A' <= c && c <= 'Z') ||
               ('0' <= c && c <= '9');
    }

    bool isPalindrome(string s) {
        int start = 0, end = s.size() - 1;

        while (start < end) {
            if (!isAlNum(s[start])) {
                ++start;
                continue;
            }

            if (!isAlNum(s[end])) {
                --end;
                continue;
            }

            if (tolower(s[end]) != tolower(s[start])) return false;

            ++start;
            --end;

        }

        return true;
        
    }
};
