import random
import string

try:
    characters = string.ascii_letters + string.digits + string.punctuation

    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        password = ""

        for i in range(length):
            password = password + random.choice(characters)

        print("Generated Password:", password)

except ValueError:
    print("Please enter numbers only.")