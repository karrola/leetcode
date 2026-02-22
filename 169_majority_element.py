### o(nlogn)
import math 

class Solution:
    def majorityElement(self, nums) -> int:
        return sorted(nums)[math.floor(len(nums)/2)]


### o(n)
class Solution:
    def majorityElement(self, nums) -> int:
        majority = res = 0
        freq = {}

        for n in nums:
            if n not in freq: freq[n] = 1
            else: freq[n] += 1

            if freq[n] > majority: 
                majority = freq[n]
                res = n

        return res