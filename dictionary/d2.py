'''
Challenge
In the code editor, there is a dictionary called your_dict. Perform the following operations in order:

Print the dictionary itself.
Print the value of the key "a".
Print True or False depending on whether the key "d" is in the dictionary.
Reassign the value of the key "a" to 4.
Print the dictionary again.
'''

your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

print(your_dict)
print(your_dict["a"])
print("d" in your_dict)
your_dict["a"] = 4
print(your_dict) 

