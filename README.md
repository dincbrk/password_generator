# Password Wordlist Generator CLI with Turkish Character Support

A powerful command-line interface (CLI) password generator supporting Turkish characters, multiple character types, and customizable password lengths.

## Features

- Supports a wide range of character types, including lowercase/uppercase Turkish letters, digits, symbols, and combinations of these.
- Generates passwords with customizable length ranges.
- Outputs results to the CLI, a file, or both.
- Adjustable password count per generation.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-generator-cli.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-generator-cli
   ```

## Usage

The CLI tool has several customizable options. Below is a list of all available options with their defaults.

### Command-line Arguments

| Option          | Description                                                                                 | Default        |
|-----------------|---------------------------------------------------------------------------------------------|----------------|
| `--min-length`  | Minimum length of the generated password.                                                   | 4              |
| `--max-length`  | Maximum length of the generated password.                                                   | 16             |
| `-t`, `--type`  | Password type (1-15) based on the character combinations listed below.                      | 15 (all types) |
| `-c`, `--count` | Number of passwords to generate.                                                            | 1              |
| `-o`, `--output`| Output method: `cli` for console, `file` for file output, `both` for both CLI and file.     | `cli`          |
| `-f`, `--filename` | File name for saving the passwords if `file` or `both` is selected as the output method. | passwords.txt  |

### Password Types

Specify the password type with `-t` or `--type`:

1. Lowercase letters (Turkish) (e.g., `abcç`)
2. Uppercase letters (Turkish) (e.g., `ABCÇ`)
3. Digits (e.g., `123`)
4. Symbols (e.g., `+-*^`)
5. Lowercase + Uppercase (Turkish) (e.g., `aA`)
6. Lowercase + Digits (e.g., `ab12`)
7. Lowercase + Symbols (e.g., `a!^+`)
8. Uppercase + Digits (e.g., `AB12`)
9. Uppercase + Symbols (e.g., `A+%&`)
10. Digits + Symbols (e.g., `123/%`)
11. Lowercase + Uppercase + Digits (Turkish) (e.g., `Ab123`)
12. Lowercase + Uppercase + Symbols (Turkish) (e.g., `Ab&/`)
13. Lowercase letters + Digits + Symbols (e.g., `a123/&`)
14. Uppercase letters + Digits + Symbols (e.g., `AB123%&`)
15. All character types (e.g., `Ab12%&`)

### Examples

1. **Generate 5 passwords of type 15 (all character types), length between 8 and 12, output to CLI:**
   ```bash
   python password_generator.py --min-length 8 --max-length 12 --type 15 --count 5 --output cli
   ```

2. **Generate 3 passwords with uppercase letters and digits (type 8), length between 10 and 15, save to a file:**
   ```bash
   python password_generator.py --min-length 10 --max-length 15 --type 8 --count 3 --output file --filename my_passwords.txt
   ```

3. **Generate 10 passwords with lowercase letters and symbols (type 7), length between 6 and 10, output to both CLI and file:**
   ```bash
   python password_generator.py --min-length 6 --max-length 10 --type 7 --count 10 --output both
   ```

### Error Handling

- If `--min-length` is greater than `--max-length`, the program will display an error and exit.


---

Feel free to contribute or open issues if you find any bugs or have suggestions for new features.
