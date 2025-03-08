"""
Task: Below are the steps:

Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that 
integer in the minimum number of guesses.

The project ideas is on: https://www.geeksforgeeks.org/
"""
import random

# Step 1: User selects a range from A to B 

while True:

    A = int(input("Enter the upper number: "))
    B = int(input("Enter the lower number: "))
    if A > B:
        A,B = B,A

    if A == B:
        print("Change another number")
        continue
    break
    
print(f"User guesses a number from {A} to {B}")

changes = 4

user_guess_counter = 0

# Step 2: The Computer will generate a Random Number

computer_generate = random.randint(A, B)

while user_guess_counter < changes:

    user_guess = int(input("Guessing one number: "))
    user_guess_counter +=1 

    # Step 3: Let's compare 
    if user_guess == computer_generate:
            print("Congratulations")
            break
    
    elif user_guess > computer_generate:
        print("Your guess is bigger than the actual number! Try another")

    elif user_guess < computer_generate:
        print("Your guess is smaller than the actual number! Try another")

if user_guess != computer_generate:
    print(f"Game over! The correct number is {computer_generate}")    

