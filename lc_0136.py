from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:



        return





nums = [4,1,2,1,2]
my_set = set()
for i in range(len(nums)):
    if nums[i] not in my_set:
        my_set.add(nums[i])
    else:
        my_set.remove(nums[i])

print(my_set.pop())
