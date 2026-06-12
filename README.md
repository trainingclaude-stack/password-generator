# Password Generator

A Python CLI tool to generate secure passwords with a built-in strength checker.

## Features
- Password length: **5 to 30 characters**
- Includes lowercase, uppercase, digits, and symbols by default
- Strength rating: Weak / Medium / Strong / Very Strong
- Generate multiple passwords at once

## Usage

`ash
# Default (12-char password)
python password_generator.py

# Custom length
python password_generator.py -l 20

# Generate 5 passwords of length 16
python password_generator.py -l 16 -n 5

# No symbols
python password_generator.py -l 12 --no-symbols

# No digits and no uppercase
python password_generator.py -l 10 --no-digits --no-upper
`

## Options

| Flag | Description |
|------|-------------|
| -l, --length | Password length (5-30), default 12 |
| -n, --count | Number of passwords to generate |
| --no-upper | Exclude uppercase letters |
| --no-digits | Exclude digits |
| --no-symbols | Exclude symbols |

## Requirements
Python 3.6+ (no external dependencies)