# Personal Mini-Toolkit
# Week 8 Final Project


# Tool 1: Simple Calculator
# This tool asks for two numbers and an operation, then displays the result.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = first_number + second_number
            print(f"The answer is {result}.")

        elif operation == "2":
            result = first_number - second_number
            print(f"The answer is {result}.")

        elif operation == "3":
            result = first_number * second_number
            print(f"The answer is {result}.")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"The answer is {result}.")

        else:
            print("That is not a valid operation.")

    except ValueError:
        print("Please enter numbers only.")


# Tool 2: To-Do List
# This tool lets the user add, view, and remove tasks from a changing list.
def todo_list():
    tasks = []

    print("\n--- To-Do List ---")
    print("You can add, view, or remove tasks.")
    print("Type 'done' when you want to return to the main menu.")

    while True:
        action = input("\nWhat would you like to do? (add/view/remove/done): ").lower()

        if action == "add":
            task = input("Enter a task: ")

            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("Please enter a task.")

        elif action == "view":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                number = 1

                for task in tasks:
                    print(f"{number}. {task}")
                    number += 1

        elif action == "remove":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Removed: {task}")
            else:
                print(f"I couldn't find '{task}' on your list.")

        elif action == "done":
            print("Returning to the main menu.")
            break

        else:
            print("Please choose add, view, remove, or done.")


# Tool 3: Number Guessing Game
# This tool uses a loop and conditionals to help the user guess a secret number.
def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I'm thinking of a number from 1 to 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(
                    f"Correct! You guessed the number in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# Main menu
# This loop keeps displaying the menu until the user chooses Quit.
print("===================================")
print(" Welcome to My Personal Mini-Toolkit!")
print("===================================")

while True:
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("Thanks for using my Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please choose 1, 2, 3, or 4.")

