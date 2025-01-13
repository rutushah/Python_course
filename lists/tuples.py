'''
Challenge
Implement a function create_pair(name: str, age: int) -> Tuple, which should combine the name and age parameters into a tuple and return it. The tuple should contain the name as the first element and the age as the second element.
'''

from typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:
    return (name, age)
    pass

# do not modify code below this line
print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))
