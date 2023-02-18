import string
import random 

characters = list(string.ascii_letters + string.digits + string.punctuation) 

def generate_password():

    random.shuffle(characters)
    password = []

    answer_input = str(input("Would you like to generate a password? (Y/N): ").lower())

    if answer_input == "y":
        pswrd_len_input = int(input("How long should the password be?: "))

        for n in range(pswrd_len_input):
            password.append(random.choice(characters))
        return str(password)
    
    return None

print(generate_password())