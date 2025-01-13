'''
Challenge
Implement the remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int] function. It accepts a dictionary my_dict and a list of strings keys. The function should remove all the keys in the list from the dictionary and return the modified dictionary. If a key doesn't exist in the dictionary, ignore it.

Be careful: If you try to remove a key that doesn't exist, it will raise a KeyError. Make sure to handle this case by checking if the key exists before trying to remove it, or using the second argument of the pop() function.
'''

from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for k in keys:
        if k in my_dict:
        #    my_dict.pop(k)
            del my_dict[k]
    return my_dict



# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
