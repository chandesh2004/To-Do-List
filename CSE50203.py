import random
import string

def generate_strong_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage: Generate a strong password of length 16
strong_password = generate_strong_password(16)
print(f"Strong Password: {strong_password}")
