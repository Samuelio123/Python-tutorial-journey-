# More on reading and writing files.
from sys import argv
script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want it, hit RETURN.")
# this is just normal input
input("?")

# in line  a file is been opened and stuffs are written inside it with function 'w'
print("Opening the file...")
target = open(filename, 'w')

# the funtion 'truncate' empty whatever is in a file.
print('Truncate the file. Goodbye!')
target.truncate()

print("Now I am going to ask your for three lines.")
# the next three lines ask for the inputs.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write this to the file.")

# In the next lines the input are written down.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print('And finally, we close it.')
target.close
# you've closed the file.
# it is mandatory to always close a file after opening it.
