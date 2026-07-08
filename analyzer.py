import string
import random

# Common weak passwords
common_passwords = [
    "123456",
    "12345678",
    "password",
    "password123",
    "admin",
    "qwerty",
    "abc123",
    "111111",
    "letmein",
    "welcome"
]


def analyze_password(password):

    score = 0
    suggestions = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Number
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    # Special Character
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!,@,#,$,%,&, etc.).")

    # Common Password
    if password.lower() in common_passwords:
        suggestions.append("This is a common password. Choose a more unique password.")
        score = min(score, 2)

    # Strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    percent = score * 20

    return score, strength, suggestions, percent


def generate_strong_password(length=12):

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ''.join(random.choice(
        string.ascii_letters +
        string.digits +
        string.punctuation
    ) for _ in range(length - 4))

    password = upper + lower + digit + special + remaining

    password = list(password)
    random.shuffle(password)

    return ''.join(password)