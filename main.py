import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(
        random.choice(characters) for _ in range(length)
    )
    return password

length = int(input("Enter password length: "))

if length < 1:
    print("Password length must be at least 1.")
else:
    password = generate_password(length)
    print("Your generated password is:", password)
