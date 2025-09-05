# password_gen.py
import random
import string

def generate(length=12, symbols=True):
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

print(generate(16))  # Например: aB3$kL9@mN2!
