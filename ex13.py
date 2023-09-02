# Prompting with the use of 'Agvr' and 'Input'.
# This 'prompt' module is used to ask somthing specific from the user.
from sys import argv

script, user_name = argv
prompt = '--> '
print(f"Hi {user_name}, I'm the {script} script.")
print(f'Welcome to your interview. {script} like to ask you a few question.')

print(f"Do you like me {user_name}?.")
likes = input(prompt)

print(f"Where do you live {user_name}?.")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("What is your favourite food?.")
food = input(prompt)

print("Can you describe yourself in three words please?.")
description = input(prompt)

print("Where do you see your work in the next 5 years?.")
years = input(prompt)


print(f"""
Alright, so you said '{likes}' about liking me.
You live in {lives}. Not sure where that is.
You have a {computer} computer. Nice.
So you love {food}, Interesting.
{description}. Wow, I would really love to meet you.
{years}. I hope your vision comes through. 
""")
