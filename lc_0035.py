from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums_len = len(nums)
        for i in range(nums_len):
            if target <= nums[i]:
                return i
            
            
        return nums_len