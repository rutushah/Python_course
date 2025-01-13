'''
Implement the function list_to_set(nums: List[int]) -> Set[int]. It should take a list of integers and return a set containing the unique elements from the list. The order the elements appear in the set does not matter.
'''

from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    myset = set()
    for n in nums:
        myset.add(n)
    return myset
    

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
