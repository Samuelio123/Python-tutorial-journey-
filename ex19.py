# Functions and Files

#in line 3, I import the module 'argv' to the system
from sys import argv
# the next line, I am assigning 'argv' to variable script and input_file
script, input_file = argv 
 # line 7, I defined 'print_all' as a function and line 8 printed the file 'f' to read
def print_all(f):
    print(f.read())
# 
def rewind(f):
    f.seek(0)
# I am calling on function print_all and it is given to 
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)    

print("First let's print the whole file:\n")

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
