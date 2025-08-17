# Write a python program to display a user entered name followed by Good Afternoon using input() function

name = input("Please enter your name: ")
print("Good Afternoon ," + name)

# Write a program to fill in a letter template given below with name and date.
letter = '''
       Dear <|name|>,
       You are selected!
       <|Date|>
       '''

name = input("Enter your name: ")
date = input("Enter the date: ")
filled_letter = letter.replace("<|name|>", name)
filled_letter = letter.replace("<|date|>", date)
print("\n-----Your Letter-----")
print(filled_letter)

# ans = print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24 September 2050"))

# Write a program to detect double space in a string.

text = input("Enter a string: ")
if "  " in text:
    print("Double space detected!")
else:
    print("No double space found.")

# Replace the double space from problem 3 with single spaces.

text = input("Enter a string: ")
updated_text = text.replace("  ", " ")
print("\nUpdated string: ")
print(updated_text)

# Write a program to format the following leter using escape sequence characters.
Letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry, this python course is nice. Thanks!"
formatted_letter = "Dear Harry, \n\tThis Python course is nice.\nThanks!"
print(formatted_letter)
