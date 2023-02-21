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
print()
print(f"Password: {generated_password}")

possible_chars = len(string.ascii_letters + string.digits + "!@#$%^&*()")
password_length = len(generated_password)
password_entropy = password_length * log2(possible_chars)
attempts_needed = round(2**password_entropy)

print()

if password_entropy > 50:
    print("Strong password")
else:
    print("Weak password")

print()
print(f"It would take {attempts_needed} attepmts to brute force attack this password.")
print()

# password is secure when ent > 50
# N = 2^E