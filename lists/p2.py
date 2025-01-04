'''
Challenge
In the code editor, implement the following two functions:

check_list_empty(my_list) -> bool should return a boolean representing whether the list is empty or not.
check_element_in_list(my_list, element) -> bool should return a boolean representing whether the element is present in the list or not. The list may contain integers or strings.
'''

def check_list_empty(my_list) -> bool:
    if len(my_list) > 0:
        return False
    else: 
        return True
    pass


def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        return True
    else: 
        return False
    pass


# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1, 2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))

print(check_element_in_list(["Apple", "Banana", "Orange"], "Banana"))
print(check_element_in_list(["Apple", "Banana", "Orange"], "Grape"))
