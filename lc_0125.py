from curses.ascii import isalnum


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i<j:
            str_i = s[i]
            str_j = s[j]
            if str_i.isalnum() and str_j.isalnum():
                if str_i.lower() != str_j.lower():
                    return False
                else:
                    i+=1
                    j-=1



            if not str_i.isalnum():
                i+=1
            if not str_j.isalnum():
                j-=1

        return True 

s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))

# def isPalindrome(self, s):
#     l, r = 0, len(s)-1
#     while l < r:
#         while l < r and not s[l].isalnum():
#             l += 1
#         while l <r and not s[r].isalnum():
#             r -= 1
#         if s[l].lower() != s[r].lower():
#             return False
#         l +=1; r -= 1
#     return True
