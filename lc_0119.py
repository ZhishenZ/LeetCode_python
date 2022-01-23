from typing import List 

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        this_index = 2
        return_array = [1,1]

        while this_index <= rowIndex:

            for i in range(this_index-1):
                return_array.insert(0,return_array.pop()+return_array[-1])
            
            return_array.insert(0,1)
            this_index +=1

        return return_array

solution = Solution()

print(solution.getRow(3))