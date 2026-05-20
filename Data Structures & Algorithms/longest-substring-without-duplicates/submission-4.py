class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        char_set = set()
        max_sub = 0
        help = 0

        for i in range(0, len(s)):
            help = 0
            char_set.clear()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                help += 1
                char_set.add(s[j])

            max_sub = max(max_sub, help)

        return max_sub

        