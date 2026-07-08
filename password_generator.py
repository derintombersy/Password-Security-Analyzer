import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password