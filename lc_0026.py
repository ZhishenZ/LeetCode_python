

from typing import List


nums = [0,0,1,1,1,2,2,3,3,4]



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums[:len(s)] = sorted(s)

        return len(s)


solution = Solution 
return_value = solution.removeDuplicates(solution,nums)
print(nums)
print(return_value)