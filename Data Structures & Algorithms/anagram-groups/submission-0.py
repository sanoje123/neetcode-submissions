class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_groups = defaultdict(list) # map charCount to list of Anagrams / defaultdict(list) automatically creates an empty list for a new anagram key, so you can directly call .append(s) without getting a KeyError

        for s in strs:
            string_cahr = [0] * 26
            
            for c in s:
                string_cahr[ord(c) - ord('a')] += 1

            ana_groups[tuple(string_cahr)].append(s)   # list can`t be a key

        return list(ana_groups.values())


        