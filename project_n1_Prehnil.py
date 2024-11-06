TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}


print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Miloslav Přehnil
email: milosprehnil@gmail.com
discord: bigburtmajlos
""")


jmeno = input("username: ")
heslo = input("password: ")

counter = 0
title_case_counter = 0
uppercase_counter = 0
lower_case_counter = 0
digit_counter = 0
sum_numeric = 0
slovnik = dict()


if jmeno in registered_users and heslo == registered_users[jmeno]:
    print("-"*40)
    print(f"Welcome to the app, {jmeno}! \nWe have 3 texts to be analyzed.")
    print("-"*40)
    user_vstup = input("Enter a number between 1 and 3 to select: ")
    if user_vstup.isdigit():
        user_vstup = int(user_vstup)
        if user_vstup >= 1 and user_vstup <= 3:
            for word in TEXTS[user_vstup - 1].split():
                length = len(word)
                occurence = slovnik.get(length, 0)
                slovnik[length] = occurence + 1
                max_occurences = max(slovnik.values())
                # Pocet slov
                counter += 1
                # Jaky typ slova
                if word.istitle():
                    title_case_counter += 1
                if word.isalpha() and word.isupper():
                    uppercase_counter += 1
                if word.islower():
                    lower_case_counter += 1
                if word.isdigit():
                    digit_counter += 1
                if word.isnumeric():
                    sum_numeric += int(word)
            print(f"There are {counter} words in the selected text.")
            print(f"There are {title_case_counter} titlecase words.")
            print(f"There are {uppercase_counter} uppercase words.")
            print(f"There are {lower_case_counter} lowercase words.")
            print(f"There are {digit_counter} numeric strings.")
            print(f"The sum of all the numbers is: {sum_numeric}")
            print("-"*40)
            print(f"{"LEN|":<3} {"OCCURENCES":^{max_occurences}} |NR")
            print("-"*40)

            for i in sorted(slovnik.keys()):
                length = i
                pocet = slovnik[i]
                print(f"{length:>3}| {"*"*pocet:<{max_occurences}} |{pocet:<1}")
        else:
            print("Number out of range. Terminating the program...")
    else:
        print("Invalid input. Terminating the program...")
else:
    print("Unregistered user. Terminating the program...")
