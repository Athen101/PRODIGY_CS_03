import re

def password_strength(password):
    
    if not re.search(r'[a-z]', password):
        print("Password should contain at least one lowercase letter.")

    if not re.search(r'[A-Z]', password):
        print("Password should contain at least one uppercase letter.")

  
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password should contain at least one special character.")

  
    if not re.search(r'\d', password):
        print("Password should contain at least one number.")

    if len(password) < 8:
        print("Password should be at least 8 characters long.")
    else:
        print("Entered password is strong!")

    


password = input("Enter your password: ")
feedback = password_strength(password)
