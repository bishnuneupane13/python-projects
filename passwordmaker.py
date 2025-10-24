chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+!~`-={}[]|:;'<>,.?/"
import random
def generate_password():
    length = int(input("Enter the desired password length: "))

    if length < 8:
        print("Password length should be at least 8 characters.")
        return generate_password()
    else:
        password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Generated password:", password)


generate_password()
