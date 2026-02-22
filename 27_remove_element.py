class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j -= 1
            elif nums[i] != val:
                i += 1
            else:
                j -= 1

        return i