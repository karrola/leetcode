### 1
class Solution:
    def longestConsecutive(self, nums) -> int:
        sorted_nums = sorted(set(nums))
        sequence = []
        start = 0
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] - sorted_nums[i] > 1: 
                sequence.append(i - start + 1)
                start = i + 1
            if i == len(sorted_nums) - 2 and sorted_nums[i + 1] - sorted_nums[i] == 1:
                sequence.append(i - start + 2)
        
        if sequence == []: return len(sorted_nums)

        return max(sequence)
    
### 2, more clear
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in nums:
                i = 1
                x = num + 1

                while x in nums:
                    i += 1
                    x += 1 

                res = max(res, i)
        return res