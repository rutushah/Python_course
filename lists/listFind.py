'''
Challenge

Challenge
Implement the find_index(nums: List[int], target: int) -> int function. It should return the index of the first occurrence of the target number in the list. You may assume that the target number will always be present in the list.

If you want a challenge, try to implement the function without using the built-in index() method.
'''

from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    # return nums.index(target) -- using index function 

    #the below code is without using index function
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
    pass


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

