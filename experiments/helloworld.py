"""helloworld.py - A first attempt at programming"""

# author: Wes Modes <wmodes@csumb.edu
# date: fdsjlfj
# license: MIT 1.0

print("Hello, World")

user_input = int(input("Enter a rating: "))

if user_input == 5:
    print("That was a five! Yay for fives.")
elif user_input > 10:
    print("That's pretty high")
else:
    print("thanks")