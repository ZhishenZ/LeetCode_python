from multiprocessing.connection import answer_challenge


class Solution:
    def reverseBits(self, n: int) -> int:

        input = n
        input_bin_str = str(bin(input))
        input_bin_str = input_bin_str[2:]
        # print(input_bin_str)

        input_bin_str_len = len(input_bin_str)

        # input_reversed_bin_str = "0"*32
        input_reversed_bin_str = input_bin_str[::-1] + "0"*(32-input_bin_str_len)
        # print(input_reversed_bin_str)
        # print(len(input_reversed_bin_str))

        base = 1
        answer = 0
        for i in reversed(range(32)):
            answer += base * int(input_reversed_bin_str[i])
            base *= 2


        return answer



solutoin = Solution()

print(solutoin.reverseBits(43261596))




