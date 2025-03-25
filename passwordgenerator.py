import random
import string

def smart_password(length):
    if length < 14:
        length = 14

    first_part = ''.join(random.choices(string.ascii_uppercase, k=2)) 
    middle_part = ''.join(random.choices(string.digits, k=2))  
    special_char = random.choice("!@#$%^&*")  
    remaining_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length-5))  

    password = first_part + middle_part + special_char + remaining_part
    return ''.join(random.sample(password, len(password)))  


length = int(input("Enter password length: "))
print("Generated Smart Password:", smart_password(length))