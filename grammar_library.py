"""This is a library of functions used to make sentences more grammatically
correct.
"""


# Function to add an article adjective to a word.
def add_article(word):
    # Define a list of vowels.
    vowels = ["a", "e", "i", "o", "u"]

    # Return "an" + the word if it starts with a vowel; else, "a" + the word.
    if word[:1] in vowels:
        return f"an {word}"
    else:
        return f"a {word}"


# Function to punctuate a list of items as a sentence.
def punctuate_list(list_of_items, title=False, conjunction="and", ending="."):
    # Convert all items into strings so they can be concatenated.
    items = [str(item) for item in list_of_items]
    message = ""

    if len(items) == 0:
        return "Nothing in list."

    # Loop through the list.
    for i in range(len(items)):
        # Define the item. I had to rewrite because .index() only finds the
        # first occurrence.
        item = items[i]

        # If it's before the next-to-last place, add a comma to the end.
        if i < len(items) - 2:
            if title:
                message += f"{item.title()}, "
            else:
                message += f"{item}, "

        # If it's the next to last place, add "and".
        elif i < len(items) - 1:
            # Omit the comma if the list length is two.
            if len(items) == 2:
                if title:
                    message += f"{item.title()} {conjunction} "
                else:
                    message += f"{item} {conjunction} "
            else:
                if title:
                    message += f"{item.title()}, {conjunction} "
                else:
                    message += f"{item}, {conjunction} "

        # If it's the last place, add a period and a newline.
        else:
            if title:
                message += f"{item.title()}{ending}"
            else:
                message += f"{item}{ending}"

    # Return the message.
    return message
