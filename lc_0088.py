

from math import inf
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return 
        p1 = 0
        p2 = 0

        nums1[m:m+n] = n*[inf]

        while p1 < (m+n):
            
            if nums2[p2] < nums1[p1]:
                    nums1.insert(p1,nums2[p2])
                    nums1.pop()
                    if p2 == n -1:
                        break
                    else:
                        p2 +=1
            p1+=1
            
            

solution = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

nums3 = [2,0]
m = 1
nums4 = [1]
n =1

solution.merge(nums3, m, nums4,n)
print(nums1[0])
# print(nums1)