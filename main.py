import random
import string

def generate_password(length: int = 10):

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(alphabet) for i in range(length))
    return password

print("Here is random password:")
print(generate_password(12))
