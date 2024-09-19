# Inform the user of whether or not the chosen number is a multiple of ten.
number = int(input("Pick a number: "))
print()

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
print("This is even easier to check than evens or odds...")