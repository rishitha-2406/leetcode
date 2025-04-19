from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        
        count = 0
        n = len(nums)
        

        for i in range(n):

            
            lower_bound = lower - nums[i]
            upper_bound = upper - nums[i]
            
            
            left = bisect_left(nums, lower_bound, i + 1, n)
           
            right = bisect_right(nums, upper_bound, i + 1, n)
            
           
            count += right - left
        
        return count
