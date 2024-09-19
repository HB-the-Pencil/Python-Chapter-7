# Ask users for their ages and print the cost of their tickets.
prompt = "Enter your age to get a ticket price."
prompt += '\n(Enter "quit" to quit the program.) '

while True:
    age = input(prompt)

    if age == "quit":
        print("Enjoy the show!")
        break

    if int(age) < 3:
        print("Your ticket is free!\n")
    elif int(age) < 12:
        print("Your ticket is $10.\n")
    else:
        print("Your ticket is $15.\n")