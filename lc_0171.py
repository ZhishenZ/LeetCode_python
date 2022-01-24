


from multiprocessing.connection import answer_challenge


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:



        my_dict = {
                   'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8, 'I':9,'J':10,'K':11, 'L':12, 'M':13, 
                   'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26
                   }






        l = len(columnTitle)
        base = 1

        columnTitle = columnTitle[::-1]
        answer = 0
        for i in range(l):
            answer += my_dict[columnTitle[i]] * base
            base *=26


        return answer







solution = Solution()
print(solution.titleToNumber("AZ"))#52
print(solution.titleToNumber("A")) #A
print(solution.titleToNumber("AB")) #28
print(solution.titleToNumber("ZY")) #701