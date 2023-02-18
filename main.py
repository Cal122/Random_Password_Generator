import string
import random 
from math import log2, log1p

def generate_password():

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()") 
    random.shuffle(characters)
    password = []

    answer_input = str(input("Would you like to generate a password? (Y/N): ").lower())

    if answer_input == "y":
        
        pswrd_len_input = int(input("How long should the password be?: "))
        while pswrd_len_input <= 0:
            pswrd_len_input = int(input("How long should the password be?: "))

        for n in range(pswrd_len_input):
            password.append(random.choice(characters))
        return "".join(password)
    
    return None

generated_password = generate_password()

print(generated_password)

possible_chars = len(string.ascii_letters + string.digits + "!@#$%^&*()")
password_length = len(generated_password)
password_entropy = password_length * log2(possible_chars)

print(password_entropy)
# password is secure when ent > 50