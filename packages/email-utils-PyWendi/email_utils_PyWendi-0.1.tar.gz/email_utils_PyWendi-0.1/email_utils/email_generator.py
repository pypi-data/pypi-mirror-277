import string
import random


def generate_random_email(domain="exemple.com"):
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{local_part}@{domain}"
