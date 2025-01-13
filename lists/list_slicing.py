'''
Challenge
Implement the function get_last_three_elements(my_list: List[int]) -> List[int]. It should return a list containing the last three elements of my_list. You may assume that the length of my_list will always be at least three.

'''

from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    # return my_list[-3:] 
    #  or normal tradition
    method_tradition = len(my_list) - 3
    return my_list[method_tradition : ]

    pass


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
