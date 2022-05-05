import random
import os

def select_word():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as words_list:
        for line in words_list:
            words.append(line.rstrip())

    random_word = random.choice(words)
    return random_word


def check_letter(word):
    lifes = 6
    hang_pic = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    special_char = ['á', 'é', 'í', 'ó', 'ú','ü']
    accepted_char = alphabet + special_char
    user_letter_list = ["_" for i in range(len(word))]
    # for spaces in range(len(word)):
    #     user_letter_list.append("_")
    actual_word= "".join(user_letter_list)
    os.system("clear")
    
    while actual_word != word and lifes > 0:
        # os.system("clear")
        print("ADIVINA LA PALABRA!!!")
        draw_man(lifes, hang_pic)
        print(actual_word.upper().replace("", " "))
        print("")
        try: 
            user_letter = input("Ingresa una letra: ").lower()
            if len(user_letter) > 1:
                raise ValueError("Solo puedes ingresar una letra a la vez")
            if user_letter.isnumeric() or user_letter not in accepted_char:
                raise TypeError("Solo puedes ingresar letras")
            if user_letter not in word:
                lifes -= 1
                hang_pic += 1
            for count, letter in enumerate(word):
                if user_letter == letter:
                    user_letter_list[count] = user_letter
            actual_word= "".join(user_letter_list)
            os.system("clear")
        except TypeError as te:
            os.system("clear")
            print(te)
            print("")
        except ValueError as ve:
            os.system("clear")
            print(ve)
            print("")

    # print(actual_word.upper())
    if lifes > 0:
        os.system("clear")
        print("ADIVINA LA PALABRA!!!")
        draw_man(lifes, hang_pic)
        print(actual_word.upper().replace("", " "))
        print("")
        print("¡Ganaste! La palabra es " + word.upper())
        print("")
    else:
        os.system("clear")
        print("ADIVINA LA PALABRA!!!")
        draw_man(lifes, hang_pic)
        print(actual_word.upper().replace("", " "))
        print("")
        print("NO TE QUEDAN VIDAS!!!\n")
        print("La palabra era " + word.upper() + "\n")
        print("JUEGO FINALIZADO")
        print("")

def draw_man(lifes, hang_pic):
    hang_pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

    print("Intentos restantes: " + str(lifes))
    print(hang_pics[hang_pic])
    print("")


def run():
    repeat = True
    while repeat:
        word = select_word()
        # print(word)
        check_letter(word)
        repeat_game = ""
        while repeat_game != 's' and repeat_game != 'n':
            repeat_game = input("¿Quieres jugar otra vez? S/N: ").lower()
            if repeat_game == 's':
                repeat = True
            elif repeat_game == 'n':
                repeat = False
            else:
                # os.system("clear")
                print("Solo puedes seleccionar S o N")
                print("")
    print("")
    print("HASTA LUEGO...")
    print("")


if __name__ == '__main__':
    run()