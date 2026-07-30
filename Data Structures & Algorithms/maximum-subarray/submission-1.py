class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # my first solution:
        # max_sum = -1100
        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i, len(nums)):
        #         cur_sum += nums[j]
        #         max_sum = max(max_sum, cur_sum)
        # return max_sum


        # Best solution
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum

