import argparse
import random
import string
import sys

# Turkish character sets
turkish_lowercase = "abcçdefgğhıijklmnoöprsştuüvyz"
turkish_uppercase = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

# Dictionary for password types, including Turkish characters
PASSWORD_TYPES = {
    1: turkish_lowercase,
    2: turkish_uppercase,
    3: string.digits,
    4: string.punctuation,
    5: turkish_lowercase + turkish_uppercase,
    6: turkish_lowercase + string.digits,
    7: turkish_lowercase + string.punctuation,
    8: turkish_uppercase + string.digits,
    9: turkish_uppercase + string.punctuation,
    10: string.digits + string.punctuation,
    11: turkish_lowercase + turkish_uppercase + string.digits,
    12: turkish_lowercase + turkish_uppercase + string.punctuation,
    13: turkish_lowercase + string.digits + string.punctuation,
    14: turkish_uppercase + string.digits + string.punctuation,
    15: turkish_lowercase + turkish_uppercase + string.digits + string.punctuation,
}

# Password generation function with uniqueness check
def generate_unique_password(min_length, max_length, charset, existing_passwords):
    while True:
        length = random.randint(min_length, max_length)
        password = ''.join(random.choice(charset) for _ in range(length))
        # Ensure the password is unique
        if password not in existing_passwords:
            existing_passwords.add(password)
            return password

# Main function
def main():
    parser = argparse.ArgumentParser(
        description="A Powerful Password Generator for CLI with Turkish Character Support",
        epilog=(
            "Example Usage:\n"
            "1. CLI output only:\n"
            "   python password_generator.py --min-length 8 --max-length 12 --type 15 --count 5 --output cli\n\n"
            "2. Output to file only:\n"
            "   python password_generator.py --min-length 10 --max-length 15 --type 8 --count 3 --output file --filename my_passwords.txt\n\n"
            "3. Both CLI and file output:\n"
            "   python password_generator.py --min-length 6 --max-length 10 --type 7 --count 10 --output both\n\n"
            "Note: Refer to 'PASSWORD_TYPES' dictionary for password type explanations."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--min-length", type=int, default=4,
        help="Specify minimum password length (default: 4)."
    )
    parser.add_argument(
        "--max-length", type=int, default=16,
        help="Specify maximum password length (default: 16)."
    )
    parser.add_argument(
        "-t", "--type", type=int, choices=PASSWORD_TYPES.keys(), default=15,
        help=(
            "Select password type (default: 15):\n"
            "  1  - Lowercase letters (includes Turkish characters) (e.g., aaa)\n"
            "  2  - Uppercase letters (includes Turkish characters) (e.g., AAA)\n"
            "  3  - Digits only (e.g., 123)\n"
            "  4  - Symbols only (e.g., +-*!)\n"
            "  5  - Lowercase + Uppercase letters (includes Turkish characters) (e.g., aA)\n"
            "  6  - Lowercase letters + Digits (e.g., ab12)\n"
            "  7  - Lowercase letters + Symbols (e.g., a!^+)\n"
            "  8  - Uppercase letters + Digits (e.g., AB12)\n"
            "  9  - Uppercase letters + Symbols (e.g., A+%%&)\n"
            " 10  - Digits + Symbols (e.g., 123/%%&)\n"
            " 11  - Lowercase + Uppercase letters + Digits (includes Turkish characters) (e.g., Ab123)\n"
            " 12  - Lowercase + Uppercase letters + Symbols (includes Turkish characters) (e.g., Ab&/)\n"
            " 13  - Lowercase letters + Digits + Symbols (e.g., a123/&)\n"
            " 14  - Uppercase letters + Digits + Symbols (e.g., AB123%%&/)\n"
            " 15  - All character types (includes Turkish characters) (e.g., Ab12%%&)"
        )
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1,
        help="Specify the number of passwords to generate (default: 1)."
    )
    parser.add_argument(
        "-o", "--output", choices=["cli", "file", "both"], default="cli",
        help="Specify output type: cli (to console), file (to file), both (console and file) (default: cli)."
    )
    parser.add_argument(
        "-f", "--filename", type=str, default="passwords.txt",
        help="Specify the filename for file output (default: passwords.txt)."
    )

    args = parser.parse_args()

    # Validate min_length and max_length
    if args.min_length > args.max_length:
        print("Error: Minimum length cannot be greater than maximum length.")
        sys.exit(1)

    # Get the selected character set
    charset = PASSWORD_TYPES.get(args.type)
    if not charset:
        print("Invalid password type selected.")
        sys.exit(1)

    # Set to store unique passwords
    unique_passwords = set()

    # Generate unique passwords
    passwords = [generate_unique_password(args.min_length, args.max_length, charset, unique_passwords) for _ in range(args.count)]

    # Handle output
    if args.output in ["cli", "both"]:
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)

    if args.output in ["file", "both"]:
        with open(args.filename, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        print(f"\nPasswords saved to {args.filename}.")

if __name__ == "__main__":
    main()
