class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper (input: int) -> int:
            output = 0
            while input:
                output += (input%10)*(input%10)
                input = input//10

            return output

        my_set = set()

        while(True):
            if n == 1:
                return True
            elif n in my_set:
                return False
            my_set.add(n)
            n = helper(n)


class Solution2:
    def isHappy(self, n: int) -> bool:
        
        n_str = str(n)

        my_set = set()#set of int

        while(1):
            cur_num = 0
            for char in n_str:
                cur_num += int(char)**2
            if cur_num == 1:
                return True
            else:
                if cur_num in my_set:
                    return False

            my_set.add(int(n_str))
            n_str = str(cur_num)


        return 

