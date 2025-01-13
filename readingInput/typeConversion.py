'''
Challenge
Implement the following two functions:

read_integer() -> int: This function should read an integer from the user and return it. The prompt should be empty.
read_float() -> float: This function should read a floating point number from the user and return it. The prompt should be empty.
'''

def read_integer() -> int:
   read_int_line = int(input())
   return read_int_line

def read_float() -> float:
   read_float_line = float(input())
   return read_float_line


# do not modify below this line
print(read_integer())
print(read_integer())
print(read_integer())

print(read_float())
print(read_float())
print(read_float())
