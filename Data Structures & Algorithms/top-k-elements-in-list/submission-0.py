from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = defaultdict(int)

        for num in nums:
            frequency_table[num] += 1

        result = []

        sorted_values = sorted(frequency_table.values(), reverse = True)[:k]

        for key, value in frequency_table.items():
            if value in sorted_values:
                result.append(key)

        return result

        