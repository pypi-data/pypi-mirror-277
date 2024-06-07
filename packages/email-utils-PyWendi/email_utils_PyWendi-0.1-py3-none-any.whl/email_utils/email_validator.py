import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def extract_domain(email):
    if not is_valid_email(email):
        raise ValueError("Invalid email address")
    return email.split("@")[1]
