



from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return [[]]

        if numRows == 1:
            return [[1]]

        return_array =  [[1],[1,1]]
        if numRows == 2:
            return return_array

        for i in range(numRows-2):
             
            list_with_one = [1]
            for j in range(i+1):
                list_with_one.append(return_array[-1][j] + return_array[-1][j+1])
            
            list_with_one.append(1)
            return_array.append(list_with_one)
        


        return return_array

solution = Solution()

print(solution.generate(5))