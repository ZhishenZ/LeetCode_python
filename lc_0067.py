class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        answer = ""
        added_term = 0
        
        while a or b:
            if a:
                val_a = int(a[-1])
                a = a[:-1]
            else:
                val_a = 0


            if b:
                val_b = int(b[-1])
                b = b[:-1]
            else:
                val_b = 0

            sum_term = added_term + val_a + val_b
            if (sum_term) >1:
                answer += str((sum_term)%2)
                added_term = 1
            else:
                answer += str(sum_term)
                added_term = 0

        if added_term:
            answer += "1"
        
        return(answer[::-1])


        # carry = 0
        # result = ''

        # a = list(a)
        # b = list(b)

        # while a or b or carry:
        #     if a:
        #         carry += int(a.pop())
        #     if b:
        #         carry += int(b.pop())

        #     result += str(carry %2)
        #     carry //= 2

        # return result[::-1]