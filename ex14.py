# READING FILES.
# line 3 imports the module 'argv' to the system
from sys import argv
# script and filename is assigned to "argv"
script, filename = argv
# in line 7 the command (open) opens a file
txt = open(filename)
print(f"Here's your file - {filename}:")
#in the next line the function 'read' lets the user read the content of the file
print(txt.read())


print("Type the filename again:")
file_again = input("--> ")
# in line 17, the inputed file is now opened again and then printed out for reading in line 18
txt_again = open(file_again)

print(txt_again.read())
# I am improving day by day.
