# Ask the user for a list of toppings and add them to the pizza one at a time.
prompt = "What topping would you like to add to your pizza?"
prompt += '\n(Type "quit" to quit.) '

while True:
    topping = input(prompt)
    if topping == "quit":
        print("Your pizza's done!")
        break
    elif topping == "pineapple":
        print("You disgust me.")
        break

    print(f"Adding {topping}...\n")