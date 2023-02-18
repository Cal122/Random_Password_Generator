import string
import random 


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