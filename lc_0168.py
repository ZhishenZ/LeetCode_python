class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        
        
        my_dict = {
                    1:'A',
                    2:'B',
                    3:'C',
                    4:'D',
                    5:'E',
                    6:'F',
                    7:'G',
                    8:'H', 
                    9:'I',
                    10:'J',
                    11:'K', 
                    12:'L', 
                    13:'M', 
                    14:'N', 
                    15:'O', 
                    16:'P', 
                    17:'Q', 
                    18:'R', 
                    19:'S', 
                    20:'T', 
                    21:'U', 
                    22:'V', 
                    23:'W', 
                    24:'X', 
                    25:'Y', 
                    26:'Z'
                    }
        
        
        input = columnNumber
        upper_bound = 26
        digits_n = 1
        answer = ""

        while(input > upper_bound):

            upper_bound = upper_bound + upper_bound*26
            digits_n += 1

        #print(digits_n) 

        for i in reversed(range(digits_n)):
            cur_base = 26**i
            if i == 0:
                largest_digit = input
            else:
                largest_digit = (input - 1)// cur_base
            input = input - largest_digit * cur_base
            answer += my_dict[largest_digit]



        return answer

solution = Solution()
print(solution.convertToTitle(52))#AZ
print(solution.convertToTitle(1)) #A
print(solution.convertToTitle(28)) #AB
print(solution.convertToTitle(701)) #AB