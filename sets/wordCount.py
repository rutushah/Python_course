'''
Implement the function count_unique_words(words: List[str]) -> int which accepts a list of strings words and returns the number of unique words in the list. It's possible the list may be empty, in which case the function should return 0.

Hint: You can call the len() function on a set to get the number of elements in the set
'''


from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    # return len(my_set)
    
    count = 0
    for w in words:
        my_set.add(w)
    return len(my_set)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
