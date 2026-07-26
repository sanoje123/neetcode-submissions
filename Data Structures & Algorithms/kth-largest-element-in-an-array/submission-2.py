import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums) - k]

        # Quick select
        # k = len(nums) - k

        # def quickSelect(l, r):
        #     pivot, p = nums[r], l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1
        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k: return quickSelect(l, p - 1)
        #     elif p < k: return quickSelect(p + 1, r)
        #     else: return nums[p]

        # return quickSelect(0, len(nums) - 1)


        target = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            pivot = nums[right]
            position = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[position], nums[i] = nums[i], nums[position]
                    position += 1

            nums[position], nums[right] = nums[right], nums[position]

            if position > target:
                return quick_select(left, position - 1)

            if position < target:
                return quick_select(position + 1, right)

            return nums[position]

        return quick_select(0, len(nums) - 1)

