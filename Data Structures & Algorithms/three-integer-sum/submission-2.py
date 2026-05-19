class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort() # first sort numbers
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            start, end = i + 1, len(nums) - 1

            target_sum = 0 - a
            
            while start < end:
                if nums[start] + nums[end] > target_sum:
                    end -= 1
                elif nums[start] + nums[end] < target_sum:
                    start += 1
                else: 
                    out.append([a, nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1

        return out
        