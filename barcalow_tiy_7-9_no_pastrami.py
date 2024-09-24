# Create a list of sandwich orders and move each sandwich to a completed list.
from grammar_library import punctuate_list

orders = ["pastrami", "egg and cheese", "turkey club", "reuben",
          "ham and swiss", "pastrami", "turkey club", "cuban", "pastrami",
          "turkey club", "pastrami", "reuben", "cuban"]
finished_sandwiches = []

# Remove pastrami from the menu.
print("Sorry, but we're out of pastrami today.")
while "pastrami" in orders:
    orders.remove("pastrami")

# Loop through the orders and complete them one at a time.
while orders:
    order = orders.pop()
    print(f"Making {order.title()}...")
    finished_sandwiches.append(order)
    print(f"Finished making {order.title()}.\n")

# Try to use the list punctuating function. (Make sure you import the most
# modern version! Chapter 6 library != Chapter 7 library.)
try:
    print("Today we made the following sandwiches:",
          punctuate_list(finished_sandwiches, True))
except NameError:
    print("Grammar library not imported.")
    print("Today we made the following sandwiches:")
    for sandwich in finished_sandwiches:
        print("  -", sandwich)