class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 1

        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                nums[j] = nums[i]
            elif nums[i - 1] == nums[i] and nums[i + 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
            elif nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
        
        return j + 1