import secrets
import string

def pass_characters(characters):
    if characters == 1:
        character_pool = string.ascii_letters
    elif characters == 2 :
        character_pool = string.ascii_letters + string.punctuation
    elif characters == 3 :
        character_pool = string.ascii_letters + string.digits
    else:
        character_pool = string.ascii_letters + string.digits + string.punctuation
    return character_pool

#Create a function to generation and assign a random password.
def genpass(length):
    password = ''.join(secrets.choice(pass_characters(characters)) for i in range(length))
    verified_cpool= pass_characters(characters)
    return password

while True:
    try:
        characters = int(input("The password configuration options are as followed:  \n\n1. Letters only \n2. Letters and Symbols \n3. Letters and Numbers  \n4. Letters, Symbols and Numbers \n\nWhat option would you like to select?: "))
        if characters >= 5 or characters <= 0:
            raise ValueError("The submitted option must be from the given options.")
        break    
    except ValueError:
        print("\nPlease select a number from the given options.")


#To accept password length and prevent illogical inputs like negative numbers, zero, and letters.
while True:
    try:
        length = int(input("Please enter your desired password length: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("\nPlease enter positive numeric values, not including '0'.\n")

def decide():
    while True:
        decision = input(f"\nPassword generated: {genpass(length)}.\nWould you like to generate another? ['Yes or 'No']: ").upper()
        if decision in ["YES", "NO"]:
            if decision == "NO":
                print("\nWondeful, Have a great day!")
                break
            else:
                continue
        else:
            continue

decide()


    





'''
 generated: {password}. Would you like to generate another? ['Yes or 'No']")

    if syn in ["Yes", "No"]:
    if syn == "Yes":
        while True:
            syn_ack = genpass(length)
            print(f"\nPassword generated: {password}.\nWould you like to generate another? ['Yes or 'No']: "
))
            break
    elif syn == "No":
        print("Wonderful. Have a great day!!")
else:
    syn = input(f"Password

'''



