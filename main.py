import random


def generate_random():

    # ambiguous letters, characters and numbers have been excluded for ease of use
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l',
               'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    characters = ['!', '@', '#', '$', '%', '^', '&', '*',
                  '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', '<', '>', ',', '.', '?', '~', '<', '>', '/', '?', '[', ']', '{', '}']

    numbers = [2, 3, 4, 5, 6, 7, 8, 9]  

    random_letter = random.choice(letters)
    random_character = random.choice(characters)
    random_number = random.choice(numbers)

    case = random.randint(0, 1)  # 0 - false; 1 - true
    if case == 1:
        random_letter = random_letter.upper()

    choice = random.randint(0, 2)

    if choice == 0:
        return random_letter
    elif choice == 1:
        return random_character
    else:
        return random_number


def generate_password(n=12):
    arr = []
    for i in range(0, n):
        arr.append(generate_random())
    psw = "".join(str(element) for element in arr)
    return psw


length = int(input("What length do you want your password to be?  "))

print(f"Your password is \n\n{generate_password(length)}\n\n")
