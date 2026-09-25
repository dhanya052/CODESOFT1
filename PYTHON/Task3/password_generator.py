"""
TASK 3 - Password Generator
CodSoft Python Programming Internship

Generates strong, random passwords of a user-specified length and
complexity (letters, digits, symbols). Uses the `secrets` module for
cryptographically-strong randomness.

Run:
    python password_generator.py
"""

import string
import secrets


def build_character_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    if not pool:
        raise ValueError("Character pool is empty — select at least one character type.")
    return "".join(secrets.choice(pool) for _ in range(length))


def ask_yes_no(prompt, default_yes=True):
    suffix = " [Y/n]: " if default_yes else " [y/N]: "
    answer = input(prompt + suffix).strip().lower()
    if not answer:
        return default_yes
    return answer.startswith("y")


def get_length():
    while True:
        raw = input("Desired password length (e.g. 12): ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a positive whole number.")


def main():
    print("===== CODSOFT PASSWORD GENERATOR =====")
    while True:
        length = get_length()
        use_upper = ask_yes_no("Include uppercase letters (A-Z)?")
        use_lower = ask_yes_no("Include lowercase letters (a-z)?")
        use_digits = ask_yes_no("Include digits (0-9)?")
        use_symbols = ask_yes_no("Include symbols (!@#$...)?", default_yes=False)

        pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols)

        try:
            password = generate_password(length, pool)
            print(f"\nGenerated Password: {password}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
            continue

        if not ask_yes_no("Generate another password?", default_yes=False):
            print("Goodbye! Stay secure.")
            break


if __name__ == "__main__":
    main()
