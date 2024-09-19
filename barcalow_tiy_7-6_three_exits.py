# Exit a loop in three different ways.

# Method 1: Conditional check
prompt = "Enter random gibberish."
prompt += '\n(Type "condition" to escape the loop.) '

user_input = ""
while user_input != "condition":
    user_input = input(prompt)
    if user_input != "condition":
        print("\tthe condition has not yet been met\n")

print("\ton to the second method!\n")

# Method 2: Event flag
prompt = "Enter random gibberish."
prompt += '\n(Type "flag" to change the flag.) '

event = True
while event:
    user_input = input(prompt)
    if user_input == "flag":
        event = False
    else:
        print("\tthe flag is still true\n")

print("\ton to the third method!\n")

# Method 3: break statement
prompt = "Enter random gibberish."
prompt += '\n(Type "break" to break out of the loop.) '

while True:
    user_input = input(prompt)
    if user_input == "break":
        break
    print("\tthe loop remains unbroken\n")

print("\ton to lunch!")