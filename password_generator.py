import random
import string

def generate_password(length):
    # characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Password length should be at least 4 for security.")
        else:
            pwd = generate_password(length)
            print("Generated Password:", pwd)
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
