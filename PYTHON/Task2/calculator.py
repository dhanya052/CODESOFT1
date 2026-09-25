"""
TASK 2 - Simple Calculator
CodSoft Python Programming Internship

Prompts the user for two numbers and an operation, performs the
calculation, and displays the result. Supports repeated calculations
in one session.

Run:
    python calculator.py
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Addition (+)", add),
    "2": ("Subtraction (-)", subtract),
    "3": ("Multiplication (*)", multiply),
    "4": ("Division (/)", divide),
}


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number, please try again.")


def print_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    print("5. Exit")


def main():
    print("Welcome to the CodSoft Simple Calculator!")
    while True:
        print_menu()
        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        label, func = OPERATIONS[choice]

        try:
            result = func(num1, num2)
            print(f"Result: {num1} {label.split('(')[-1].strip(')')} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
