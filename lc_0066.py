from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1):
            
            if digits[-i-1] + 1 == 10:
                digits[-i-1] = 0
                
            else:
                digits[-i-1] +=1
                return digits
                
                
        if digits[0] == 9:
            digits[0] = 0
            digits.insert(0,1)
        else:
            digits[0] +=1
            
            
        return digits

input =  [9,9]
solution = Solution 
return_nvalue = solution.plusOne(solution,input)
print(return_nvalue)