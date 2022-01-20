class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
        "I" : 1, 
        "V" : 5, 
        "X" : 10,
        "L" : 50, 
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
        }

        sl = len(s)
        return_val = 0
        pointer = 0
        while (pointer<sl):
            if (pointer == (sl-1)):
                return_val += dictionary[s[pointer]]
                return return_val
            if( (s[pointer]!=s[pointer+1]) and (s[pointer:pointer+2] in dictionary) ):
                return_val += dictionary[s[pointer:pointer+2]]
                pointer+=2
            else:
                return_val += dictionary[s[pointer]]
                pointer+=1

        return return_val



solution = Solution 
return_value = solution.romanToInt(solution,"LVIII")
print(return_value )