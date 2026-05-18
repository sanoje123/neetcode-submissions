class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            c1 = s[start]
            c2 = s[end]
            if not (('a' <= c1 <= 'z') or ('A' <= c1 <= 'Z') or ('0' <= c1 <= '9')):
                start += 1
                continue
            if not c2.isalnum():
                end -= 1
                continue

            if c1.lower() != c2.lower(): return False

            start += 1
            end -= 1

        return True

