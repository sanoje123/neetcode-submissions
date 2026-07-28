class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # time complexity (n * 2^n)

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # to included num[i]
            subset.append(nums[i])
            dfs(i + 1)

            # not to included num[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res