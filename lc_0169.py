

from typing import List

from numpy import MAY_SHARE_BOUNDS


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        l = len(nums)
        half = l/2
        
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] += 1
                if my_dict[element] > half:
                    return element
                

        return nums[0]


solution = Solution()

#print(solution.majorityElement([3,2,3]))

print(solution.majorityElement([1]))
