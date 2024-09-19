# Ask how many people need seats at a restaurant and inform them of the wait.
party = int(input("How many in your party? "))
print()

if party > 8:
    print("We're sorry, but all of our tables for parties of 8 are full.")
else:
    print("We have a table for you!")