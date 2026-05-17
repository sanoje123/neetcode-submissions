from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ## sorting solution:
        # frequency_table = defaultdict(int)
        # for num in nums:
        #     frequency_table[num] += 1        
        # result = []
        # sorted_values = sorted(frequency_table.values(), reverse = True)[:k]
        # for key, value in frequency_table.items():
        #     if value in sorted_values:
        #         result.append(key)
        # return result

        # bucket sort
        frequency_map = {}
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num,0)

        frequency_array = [[] for i in range(len(nums) + 1)]

        for key, value in frequency_map.items():
            frequency_array[value].append(key)

        res = []
        for i in range(len(frequency_array) - 1, 0, -1):
            for n in frequency_array[i]:
                res.append(n)
                if len(res) == k:
                    return res

            



        