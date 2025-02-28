import re

def check_password_strength(password):
    # Check password length
    length = len(password) >= 8
    # Check for uppercase letters
    uppercase = bool(re.search(r"[A-Z]", password))
    # Check for lowercase letters
    lowercase = bool(re.search(r"[a-z]", password))
    # Check for digits
    digit = bool(re.search(r"\d", password))
    # Check for special characters
    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Compile results
    criteria = {
        "length": length,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digit": digit,
        "special": special,
    }

    # Check if all criteria are met
    if all(criteria.values()):
        return "Strong password!"
    else:
        weak_reasons = [key for key, value in criteria.items() if not value]
        return f"Weak password! Missing criteria: {', '.join(weak_reasons)}"

# User input
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
