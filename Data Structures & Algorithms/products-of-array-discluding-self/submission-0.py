class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * len(nums)
        sufix_sum = [0] * len(nums)

        prefix_sum[1] = nums[0]
        sufix_sum[len(nums) - 2] = nums[len(nums) - 1]

        for i in range(2, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i - 1]
            sufix_sum[len(nums) - 1 - i] = sufix_sum[len(nums) - i] * nums[len(nums) - i]

        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = prefix_sum[i] * sufix_sum[i]

        res[0] = sufix_sum[0]
        res[len(nums) - 1] = prefix_sum[len(nums) - 1]
        return res
        