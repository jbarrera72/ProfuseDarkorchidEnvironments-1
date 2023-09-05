# String Practice:

# Create a Python program that asks the user to input a sentence.
question1= input("input any sentence ")
# Print the first and last letter of the sentence.
print(f"{question1[0]}")
print(f"{question1[-1]}")
# Convert the entire sentence to uppercase and print the result.
print(f"{question1.upper()}")
# Find and print a substring from the inputted sentence.
print(f"{question1[0:5]}")
# Replace a word in the sentence and print the updated sentence.
print()

# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
name1= input("what is your name?")
age= input("what is your age?")
movie= input("what is your favorite movie?")
# Print a message back to the user with this information.
print(f"Your name is {name1} and you are {age} years old. Your favorite movie is {movie}.")
# Note: Make sure to convert the age to an integer.

print()
# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
object1= input("name an object in the room: ")
object2= input("name a second object in the room: ")
object3= input("name a third object in the room: ")
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
print(f"In the room there is {object1}, {object2}, and {object3}.")
# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.
book= input("What is your favorite book? ")
favmovie= input("What is your favorite movie? ")
song= input("What is your favorite song? ")
# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."
print(f"Your favorite book is {book}, your favorite movie is {favmovie}, and your favorite song is {song}.")

# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."