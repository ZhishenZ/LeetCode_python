from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        mylist = []
        count = 0
        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num!= val:
                mylist.append(cur_num)
                count +=1
                
        nums[:count-1] = mylist
        
        return count