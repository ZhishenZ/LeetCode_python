from typing import List
from numpy import number

from pyparsing import nums


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        target_half = target*0.5

        p1 = 0
        p2 = len(numbers)-1

        while p1<p2:

            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]

            if ( target_half - numbers[p1]) > (numbers[p2]-target_half):
                p1 += 1

            if ( target_half - numbers[p1]) < (numbers[p2]-target_half):
                p2 -= 1


        return []
        



solution = Solution()
print(solution.twoSum([2,7,11,15],9))
print(solution.twoSum([1,2,3,4,4,9,56,90],8))
print(solution.twoSum([0,0,3,4],0))
print(solution.twoSum([2,3,4],6))
print(solution.twoSum([3,24,50,79,88,150,345],200))
