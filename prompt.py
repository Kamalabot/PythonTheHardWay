from sys import argv

script, user_name, passwd = argv
prompt = '#'

print(f"Hi {user_name}. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")

lives = input(prompt)

print(f"What kind of computer you have?")
com = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {com} computer. Nice.
""")

print("What is your password, I forgot")
password = input(prompt)

if passwd == password:
    print(f"You have a great memory {user_name}")
else:
    print(f"I am sure, scripts like me will take over soon...")