import string
import random

def generate_secure_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

    while len(password) < 8:
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)
    secure_password = ''.join(password_list)

    return secure_password

password_result = generate_secure_password()
print(f"Safe Password: {password_result}")
