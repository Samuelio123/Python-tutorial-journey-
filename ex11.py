# "Inputs".
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end =' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So you're {age} old, {height} tall and {weight} heavy.")

# Another type of input.
age = input("\nHow old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So you're {age} old, {height} tall and {weight} heavy.")

# Another example of input
name = input("\nWhat is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
age = age + 1
print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")
