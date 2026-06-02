class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ## my_solution:
        # l = 0;
        # count = {}
        # len_s1 = len(s1)

        # for s in s1:
        #     count[s] = 1 + count.get(s, 0)

        # for r in range(0, len(s2)):
        #     if s2[r] in count:
        #         count[s2[r]] -= 1
                
        #     if len_s1 < (r - l + 1):
        #         if s2[l] in count.keys():
        #             count[s2[l]] += 1
        #         l += 1

        #     if all(value == 0 for value in count.values()):
        #             return True;

        # return False


        ## Their solution
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range (len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:  #we made it to large
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:  #we made it to large
                matches -= 1

            l += 1

        return matches == 26



        