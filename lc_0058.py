class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while (s[-1]==" "):
            s = s[:-1]
        
        output = 0
        for i in range(len(s)):
            if s[-1-i]==" ":
                return output
            else:

                output +=1
            
        return output