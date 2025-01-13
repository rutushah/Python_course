'''
Implement the following two functions:

get_dict_keys(age_dict: Dict[str, int]) -> List[str] should take a dictionary of names and ages and return a list of the names.
get_dict_values(age_dict: Dict[str, int]) -> List[int] should take a dictionary of names and ages and return a list of the ages.
'''

from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    keys = []
    for key in age_dict:
        keys.append(key)
    return keys

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values = []
    for key in age_dict:
        values.append(age_dict[key])
    return values
    

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
