# 18.Jan.2022 first time

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i+1,num_len):
                if nums[i] + nums[j] ==target:
                    return [i,j]


solution = Solution 
nums = [2,7,11,15]
target = 9
return_nvalue = solution.twoSum(solution,nums,target)
print(return_nvalue)
