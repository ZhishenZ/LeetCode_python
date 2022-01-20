
class Solution:



    def isValid(self, s: str) -> bool:
        
        
        dict = {'(':')', '[':']', '{':'}'}

        stack = []

        for i in range(len(s)):
            cur_s =s[i]
            if cur_s in dict:
                stack.append(dict[cur_s])
            elif stack:
                if (cur_s!=stack.pop()):
                    return False 
            else: return False
            
            
            
        if(stack):
            return False

        return True


        


solution = Solution 
input = "{{}[][[[]]]}"
return_value = solution.isValid(solution,input)
print(return_value )







# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false