### brute force
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: return [i, j]

### szybkie
class Solution:
    def twoSum(self, nums, target: int):
        dict = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict:
                return [dict[val], i]
            else:
                dict[nums[i]] = i