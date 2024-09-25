""" Create a program that imports candy data and creates a dictionary of
dictionaries.

Allow users to access their previous input and add or remove data.

In other words, this is a basic database software. I'm guessing that we will
eventually make something similar to this that writes to a file.

TODO:
[X] Pseudocode

[X] From this data create a dictionary that holds both the students' names,
    candy, and cost they voted for in the survey.

[X] Allow students to be able to input their names into the program and see
    what candy they requested.

[X] Students should then be able to add or remove the candy. They should be
    able to do this multiple times if necessary and it should print out a
    receipt that shows their change and that it is added to the survey data.

[X] Please show me your idea and plan prior to coding anything for approval.
    (PSEUDOCODE) and layout.

This program may change as other ideas are considered by the product owner.
"""

import csv

# Pull in the CSV file
filename = 'Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    name = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []

    for row in reader:
        add_name = row[1]
        add_candy_1 = row[2]
        add_candy_2 = row[4]
        add_price_1 = float(row[3])
        add_price_2 = float(row[5])

        # Append the variables into the correct lists.
        name.append(add_name.lower().strip())
        candy_type_1.append(add_candy_1.lower().strip())
        candy_type_2.append(add_candy_2.lower().strip())
        candy_price_1.append(add_price_1)
        candy_price_2.append(add_price_2)

# The interactive part of the program begins here.
user_input = {}

# Assign the data to their respective user.
for i in range(len(name)):
    user_input[name[i]] = {candy_type_1[i]: candy_price_1[i],
                           candy_type_2[i]: candy_price_2[i]}

# Declare variables for the loop.
running = True
current_user = ""

# Print the registered users before we enter the loop.
print("Users with existing data:")
for user in user_input.keys():
    print(f"  {user.title()}")
print()

while running:
    # If the user is an empty string, ask the user for their name.
    if not current_user:
        current_user = input("Enter your name. Type QUIT to quit. > ")
        current_user = current_user.lower().strip()
        print()
        continue

    # If the user is "quit", quit the program.
    elif current_user == "quit":
        running = False
        print("Goodbye.")
        continue

    # Otherwise, if the user is in the dictionary, run the add/remove loop.
    elif current_user in user_input.keys():
        user_data = user_input[current_user]

        # Print the user's data.
        print(f"Candies in {current_user.title()}'s list:")
        for candy, price in user_data.items():
            print(f"  {candy.title()}: ${price}")
        print()

        # Get the user's add/remove input.
        add_remove = input("Add or remove items? Type QUIT to quit. > ")
        add_remove = add_remove.lower().strip()

        # Check if the user is quitting.
        if add_remove == "quit":
            current_user = ""
            print("Goodbye.\n")
            continue

        # Check if the user is adding an item.
        elif add_remove == "add":
            print()  # Add a new line.
            candy = input("Enter the name of the candy. > ")
            candy = candy.lower().strip()
            price = input("Enter the price of the candy. > ")

            # Attempt to convert the price to a float.
            try:
                price = float(price)
            except ValueError:
                print("Price needs to be a float.\n")
                continue

            # Update the dictionary.
            user_data.update({candy:price})
            print(f"Added {candy.title()} to list of candies.")
            continue

        # Check if the user is removing an item.
        elif add_remove == "remove":
            print()  # Add a new line.
            candy = input("Enter the name of the candy to be deleted. > ")
            candy = candy.lower().strip()

            # Make sure the candy can be deleted.
            if candy in user_data:
                del user_data[candy]
                print(f"Deleted {candy.title()} from list of candies.")
                continue
            else:
                print(f"{candy.title()} is not in the list of candies.\n"
                      f"Make sure you spelled it correctly.\n")
                continue

        # If the command is invalid, tell the user as much.
        else:
            print("Enter a valid command.\n")

    # If the user is not in the dictionary, add them to the dictionary.
    else:
        print(f"{current_user.title()}, you have no data.")
        print("Adding you to the list of users...\n")
        user_input[current_user] = {}
        continue