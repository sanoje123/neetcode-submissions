class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0;
        count = {}
        len_s1 = len(s1)

        for s in s1:
            count[s] = 1 + count.get(s, 0)

        for r in range(0, len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
                
            if len_s1 < (r - l + 1):
                if s2[l] in count.keys():
                    count[s2[l]] += 1
                l += 1

            if all(value == 0 for value in count.values()):
                    return True;

        return False