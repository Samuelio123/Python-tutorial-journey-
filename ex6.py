# "Strings and Texts."
types_of_people = 10   
x = f"There are {types_of_people} types of people"

Binary = "binary"
do_not = "don't"
# in the exercise am learning how to put a sting in another string which am about to do.
y = f"Those who know {Binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hillarous = True
joke_evaluation = "Isn't that jokes so funny! {}"
# this next line use a special type of formatting called (f-string).
print(joke_evaluation.format(hillarous))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# wanna try out different examples
name = "Samuelio"
real = f"{name}?, He is the best"
Real = "AM THE BEST"

A = "always striving to do all my works. And as always you can be my guest."
C = "consistently focused, never playing ...." 
# presently I am overwhelmed, and anxious.

print(f"""
Let me introduce myself, I am {name}.""")
print(f"Don't you know {real} that's why He is never compared to the rest.")
print(f"I said: {Real}.")

print(C + A)
