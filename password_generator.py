import random
import string
import argparse


MIN_LENGTH = 5
MAX_LENGTH = 30


def generate_password(length: int, use_upper: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    if not (MIN_LENGTH <= length <= MAX_LENGTH):
        raise ValueError(f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH} characters.")

    chars = string.ascii_lowercase
    required = [random.choice(string.ascii_lowercase)]

    if use_upper:
        chars += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        chars += string.punctuation
        required.append(random.choice(string.punctuation))

    remaining = [random.choice(chars) for _ in range(length - len(required))]
    password_list = required + remaining
    random.shuffle(password_list)
    return "".join(password_list)


def check_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < MIN_LENGTH:
        return "Too Short"
    if length >= 20 and score == 4:
        return "Very Strong"
    if length >= 12 and score >= 3:
        return "Strong"
    if length >= 8 and score >= 2:
        return "Medium"
    return "Weak"


def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help=f"Password length ({MIN_LENGTH}-{MAX_LENGTH}), default: 12")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate")
    args = parser.parse_args()

    try:
        for i in range(args.count):
            pwd = generate_password(
                args.length,
                use_upper=not args.no_upper,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
            )
            strength = check_strength(pwd)
            print(f"Password {i+1}: {pwd}  [{strength}]")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
