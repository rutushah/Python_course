'''
Implement the read_integers() -> List[int] function. It should read a line from stdin, without printing anything, and return a list of integers. You may assume every line will be in the following format, where the numbers are separated by commas:

1,2,3,4,5
'''

from typing import List

def read_integers() -> List[int]:
    read_int_line = (input())
    string_list = read_int_line.split(",")
    int_list = []

    for s in string_list:
        int_list.append(int(s))

    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
