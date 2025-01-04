'''
To append list, we use for loops to append elements of list as shown in the given example
Implement a function called append_to_list(my_list: List[int], elements: List[int]) -> List[int]. It should append each number from elements to the end of my_list and return the modified list.
'''

from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    for num in elements:
        my_list.append(num)
    return my_list



# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
