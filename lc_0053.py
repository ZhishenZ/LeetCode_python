from socket import SO_LINGER
from typing import List

from numpy import single


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        sum_val = nums[0]
        sum_val_global = nums[0]

        for i in range(1,len(nums)):

            cur_num = nums[i]
             
            if(cur_num)>sum_val:
                sum_val = max(cur_num, sum_val+cur_num)
            else:
                sum_val = sum_val+cur_num
            
            #sum_val = max(cur_num, sum_val+cur_num) if(cur_num)>sum_val else sum_val+cur_num
            
            sum_val_global = max(sum_val_global,sum_val)



        return sum_val_global



# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


nums = [-2,1,-3,4,-1,2,1,-5,7,9]

solution = Solution 
return_value = solution.maxSubArray(solution,nums)
print(return_value)