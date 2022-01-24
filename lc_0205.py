
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
    

        def get_word_patter( input_str):

            my_dict = {}
            index = 0
            answer = []
            for char in input_str:
                if char not in my_dict:
                    my_dict[char] = index
                    answer.append(index)
                    index +=1
                else:
                    answer.append( my_dict[char])


            return answer

        return get_word_patter( s ) == get_word_patter( t )







# test = "paper"
# my_dict = {}
# index = 0
# answer = []
# for char in test:
#     if char not in my_dict:
#         my_dict[char] = index
#         answer.append(index)
#         index +=1
#     else:
#         answer.append( my_dict[char])


# print(answer)

