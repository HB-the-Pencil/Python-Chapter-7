# Poll users on their dream vacation destination.
from grammar_library import punctuate_list

responses = {}

# Poll the users.
polling = True
while polling:
    # Get the user's input.
    name = input("Enter your name: ")
    destination = input("Where would you go on your dream vacation? ")

    # Put the response into the dictionary.
    if name in responses:
        # If the name's already in the dictionary, turn it into a list and
        # add the new location.
        if isinstance(responses[name], list):
            responses[name].append(destination)
        else:
            responses[name] = list([responses[name]])
            responses[name].append(destination)
    else:
        responses[name] = destination

    # Ask the user if they have more to input.
    y_n = input("Would you like to add another response? (y/n) ")
    if y_n == "n":
        polling = False
    print()

# Print the results of the poll.
print("\n---Results of the Poll---")
for name, location in responses.items():
    # If it's a list, punctuate the list.
    if isinstance(location, list):
        try:
            # Use the punctuate list function if it exists.
            print(f"{name.title()} would like to go to",
                  punctuate_list(location, True, "or",
                                 ""),
                  "on vacation.")
        except NameError:
            # Otherwise, print it as a bulleted list.
            print(f"{name.title()} would like to go to the following places"
                  f"for vacation:")
            for loc in location:
                print(" -", loc.title())

    # Otherwise, print the one location.
    else:
        print(f"{name.title()} would like to go to {location.title()} on "
              f"vacation.")