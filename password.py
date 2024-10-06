import os 
import secrets
import string
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation 

    password_length = secrets.randbelow(9) + 8

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    remaining_length = password_length - 4
    all_characters = lowercase + uppercase + digits + special_characters 
    password += [
        secrets.choice(all_characters) 
        for _ in range(remaining_length)
    ]

    random.shuffle(password)
    return ''.join(password)
   

def is_valid_password(password):
    if len(password) < 8 or len(password) > 16:
        print("A senha deve ter entre 8 e 16 caracteres.")
        return False
    if not any(c.islower() for c in password):
        print("A senha deve conter pelo menos uma letra minúscula.")
        return False
    if not any(c.isupper() for c in password):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    if not any(c.isdigit() for c in password):
        print("A senha deve conter pelo menos um número.")
        return False
    if not any(c in string.punctuation for c in password):
        print("A senha deve conter pelo menos um caractere especial.")
        return False
    return True
    
def show_menu():
    return input(
        "Você gostaria de gerar uma senha aleatória: (S), "
        "criar sua própria senha: (C), limpar a tela: (L) ou sair: (Q)?"
    ).strip().lower()

while True:
    user_choice = show_menu()

    if not user_choice:
        print("Entrada vazia. Por favor, insira uma opção válida.")
        continue
        

    if user_choice == "s":
        password_generated = generate_password()
        print(f"Sua senha gerada é: {password_generated}")

    elif user_choice == "c":
        while True:
            user_password = input(
                "Digite sua senha (8 a 16 caracteres, incluindo "
                "maiúsculas, minúsculas, números e caracteres especiais) "
                "ou digite 'V' para retornar ao menu: "
            ).strip()

            if user_password.lower() == 'V':
                break

            if not user_password:
                print("Entrada vazia. Por favor, insira uma senha válida.")
            elif is_valid_password(user_password):
                print("Sua senha foi criada com sucesso!")
                break
            else:
                print("A senha não atende aos requisitos. Tente novamente.")

    elif user_choice == "l":
        clear_screen()

    elif user_choice == "q":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Entrada inválida. Por favor, responda com 'S', 'C', 'L' ou 'Q'.")




