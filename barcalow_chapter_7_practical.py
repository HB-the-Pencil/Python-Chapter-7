""" This program takes user input to create a list of fast-food restaurants.

Then, it surveys 8 students on their favorite fast-food restaurants, assigning
these to lists inside a dictionary.

After that, it prints a list of inputs that matched the original list, then
adds all restaurants to a set of restaurants mentioned.

TODO:
[X] Create a list from an input that includes 5 fast food restaurants.

[X] Create a dictionary from user input and then check to see if the user
    input is in a dictionary of popular fast-food restaurants. The key should
    be the name of the student, and the values should be a list of different
    fast-food restaurants.

[X] Include 8 students' fast food restaurants in your dictionary. Write a
    while loop that will loop until 8 students have answered your survey. You
    should also create a loop that allows students to add multiple entries to
    the dictionary.

[X] Check to see If the input fast food restaurant is in your original list.
    If not on the list add it to your list. Make sure no duplicates are in
    your list.
"""

# Start by creating a title to summarize the program.
prompt = """
+======================================+
|           Restaurant Poll            |
|                                      |
| Begins by accepting a list of five   |
| fast-food restaurants from the user. |
|                                      |
| Polls 8 users on their favorite fast-|
| food restaurants and compares the    |
| results with the list.               |
+======================================+

Please input the name of the first fast-food restaurant: > """

# Begin adding items to the list. PyCharm helped me condense this code a bit.
fast_food = [input(prompt)]

# Add the last 4 items to the list.
for i in range(1, 5):
    # Ordinal numbers for ease of understanding.
    ordinal = "second" if i+1 == 2\
        else "third" if i+1 == 3\
        else "fourth" if i+1 == 4\
        else "fifth"
    fast_food.append(input(f"Please input the name of the {ordinal} "
                           f"fast-food restaurant: > ").strip().lower())

# Create a dictionary that is currently empty.
user_responses = {}
print("\n== Beginning the User Poll ==\n")

# Is a user being polled?
responding = False
user = ""

# Create a while loop that repeats 8 times.
users_responded = 0
while users_responded < 8:
    if not responding:
        # Find out who is responding to the poll.
        user = input(f"What is your name? "
                     f"(User {users_responded+1}/8) > ").strip().lower()

        # If the user has not responded, add them to the response list.
        if user not in user_responses.keys():
            user_responses[user] = []
            responding = True
        else:
            print("That user has already responded.")
    else:
        # Get an input from the user.
        user_responses[user].append(
            input("  Enter a fast-food restaurant. > ").strip().lower())

        # Continue the poll?
        y_n = input("  Enter another response? (y/n) > ").strip().lower()
        if y_n == "n":
            responding = False
            users_responded += 1
            print()

# Create a set of all responses.
unique_restaurants = set()
print("\n== Finding Matches Between Fast-Food List and Responses ==\n")

# Print out the matches between the given fast-food restaurants and the
# responses.
for user, restaurant_list in user_responses.items():
    for restaurant in restaurant_list:
        # Thank you, W3Schools. You are my hero <3
        unique_restaurants.add(restaurant)

        # If the restaurant is in the fast food list, print it.
        if restaurant in fast_food:
            print(f"{user.title()} - {restaurant.title()}")

print("\n== All Restaurants Mentioned in the Survey ==\n")
for restaurant in unique_restaurants:
    print(" -", restaurant.title())