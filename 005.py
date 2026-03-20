def check_password_strength(password):
    if len(password) < 6:
        return "Weak ❌"
    elif len(password) < 10:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)