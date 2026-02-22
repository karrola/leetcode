### works but very slow
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        numbers = {}
        for i in range(len(nums)):
            if nums[i] in numbers: numbers[nums[i]].append(i)
            else: numbers[nums[i]] = [i]
        
        for number in numbers:
            indexes = numbers[number]
            if len(indexes) > 1:
                for i in range(len(indexes) - 1):
                    for j in range(i+1, len(indexes)):
                        if abs(indexes[i] - indexes [j]) <= k: return True
        
        return False
    
### better
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = {}
        i = j = 0

        while j < len(nums):
            if k < abs(j - i):
                window[nums[i]] = None
                i += 1
            else:
                if window.get(nums[j]) == None: window[nums[j]] = 1
                else: return True
                j += 1
        
        return False