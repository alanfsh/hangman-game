import random
import os

def select_word():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as words_list:
        for line in words_list:
            words.append(line.rstrip())

    random_word = random.choice(words)
    return random_word.upper()


def draw_man(lifes, repeated_letter):
    hang_image = ["  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        ] 
    print("ADIVINA LA PALABRA!!!")
    print("Vidas: " + str(lifes))
    print(hang_image[lifes])
    print("")
    if repeated_letter:
        print("Ya utilizaste esa letra!!!")            



def game(word):
    lifes = 6

    # Characters accepted
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
    special_char = ['Á', 'É', 'Í', 'Ó', 'Ú','Ü',]
    accepted_char = alphabet + special_char
    used_letters = set()   # Used letters 
    repeated_letter = False  # If the user inputs a letter used

    found_letters = ["_"] * len(word)  # All letters found
    user_word= "".join(found_letters)  # String that contains the letters found
    os.system("clear")   

    while user_word != word and lifes > 0:
        draw_man(lifes, repeated_letter)
        print(user_word.replace("", " ") + "\n")  # Prints the incomplete word with "_"
        print("Letras utilizadas: " + ", ".join(used_letters) + "\n")  # Prints the used letters
        try: 
            letter = input("Ingresa una letra: ").upper()
            if len(letter) > 1:  # User only can type 1 character
                raise ValueError("Solo puedes ingresar una letra a la vez")

            if letter not in accepted_char:
                raise TypeError("Solo puedes ingresar letras")

            if letter in used_letters:
                repeated_letter = True

            if letter not in used_letters:
                if letter in word:
                    for index, character in enumerate(word):
                        if letter == character:
                            found_letters[index] = letter  # Replace the "_" with the user letter
                            used_letters.add(letter)  # Add letter to the used letters
                if letter not in word:
                    used_letters.add(letter)
                    lifes -= 1
                repeated_letter = False
                
            user_word= "".join(found_letters)
            os.system("clear")
    
        except TypeError as te:
            os.system("clear")
            print(te)
            print("")
        except ValueError as ve:
            os.system("clear")
            print(ve)
            print("")
    
    os.system("clear")
    draw_man(lifes, repeated_letter)
    print(user_word.replace("", " ") + "\n")
    if lifes > 0:
        print("¡Ganaste! La palabra es " + word + "\n")
    else:
        print("NO TE QUEDAN VIDAS!!!\n")
        print("La palabra era " + word.upper() + "\n")


def run():
    repeat = True
    while repeat:
        word = select_word()
        print(word)
        game(word)
        repeat_game = ""
        while repeat_game != 's' and repeat_game != 'n':
            repeat_game = input("¿Quieres jugar otra vez? S/N: ").lower()
            if repeat_game == 's':
                repeat = True
            elif repeat_game == 'n':
                repeat = False
            else:
                # os.system("clear")
                print("Solo puedes seleccionar S o N\n")
    
    print("\nHASTA LUEGO...\n")


if __name__ == '__main__':
    run()