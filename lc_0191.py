

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        input_bin_str = str(bin(n))
        input_bin_str = input_bin_str[2:]
        answer = 0
        for char in input_bin_str:
            answer += int(char)
            
        return answer
        