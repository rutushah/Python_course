'''
Implement the function count_characters(word: str) -> Dict[str, int]. It should take a string word and return a dictionary with the count of each character in the word. The keys should be the characters and the values should be the count of each character.

Hint: If you access a key that doesn't exist in a dictionary, it will raise a KeyError. Make sure to handle this case by checking if the key exists before trying to access it.

'''

from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_char_count = {}
    for char in word: 
        if char in dict_char_count:
            dict_char_count[char] += 1
        else: 
            dict_char_count[char] = 1
    return dict_char_count


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
