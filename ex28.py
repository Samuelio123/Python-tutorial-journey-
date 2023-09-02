# While Loops

i = 0
number = []
while i < 6:
    print(f"At the top i is {i}")
    number.append(i)

    i = i + 1
    print("Number now", number)
    print(f"At the top i is {i}")

print("The Number: ")
for num in number:
    print(num)
