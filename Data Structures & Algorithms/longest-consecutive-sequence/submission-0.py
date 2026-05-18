class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_hash = {num for num in nums}
        max_count = 0

        for num in number_hash:
            if(num - 1) not in number_hash:
                help_count = 1
                while(1):
                    if (num + 1) in number_hash:
                        help_count += 1
                        num += 1
                    else:
                        if help_count > max_count: max_count = help_count
                        break


        return max_count



        


        return 1

        