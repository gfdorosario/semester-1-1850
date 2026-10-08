# Week 1.2, Session 2: Task 3
# Simple Voting Eligibility Checker


# Prompt the user to enter their age
print("Welcome to the Voting Eligibility Checker!")

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if age < 0 or age > 120:
        print("Please enter a valid age.")
    else:
        break

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
