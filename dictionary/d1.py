'''
Challenge
You are given two functions to implement:

create_dict(name: str, age: int) -> Dict[str, int] should create a dict, mapping the name to the age and then return the dict.
list_to_dict(words: List[str]) -> Dict[str, int] should take a list of strings words and map each string to its index in the list, and return the resulting dict.
'''

from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    my_dict = {
        name : age
    }
    return my_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict1 = {}
    for i in range(len(words)):
        cur_word = words[i]
        my_dict1[cur_word] = i
    return my_dict1



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
