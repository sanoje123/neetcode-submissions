

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        anagrm_map = {}

        for cs in s:
            anagrm_map[cs] = anagrm_map.get(cs, 0) + 1

        for ct in t:
            anagrm_map[ct] = anagrm_map.get(ct, 0) - 1

        for value in anagrm_map.values():
            if value != 0:
                return False

        return True

        