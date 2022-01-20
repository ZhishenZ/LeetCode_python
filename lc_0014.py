

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        str_n = len(strs)

        shortest_str_len = 100

        for i in range(str_n):
            cur_len = len(strs[i])
            if (cur_len < shortest_str_len):
                shortest_str_len = cur_len


        for i in range(shortest_str_len):
            for j in range(1,str_n):
                if(strs[0][i]!=strs[j][i]):
                    return output

            
            output +=strs[0][i]

        return output

strs = ["dog","racecar","car"]

solution = Solution 
return_value = solution.longestCommonPrefix(solution,strs)
print(return_value )
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
