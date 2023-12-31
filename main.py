import datetime

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def get_salutation(langue):
    current_hour = datetime.datetime.now().hour
    if langue.lower() == 'fr':
        if 6 <= current_hour < 12:
            return "Bonjour!"
        elif 12 <= current_hour < 18:
            return "Bonjour!"
        else:
            return "Bonsoir!"
    else:
        if 6 <= current_hour < 12:
            return "Good morning!"
        elif 12 <= current_hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"

def auRevoir(langue):
    current_hour = datetime.datetime.now().hour
    if langue.lower() == 'fr':
        if 18 <= current_hour < 24:
            return "Bonne soirée!"
        else:
            return "Bonne journée!"
    else:
        if 18 <= current_hour < 24:
            return "Good night!"
        else:
            return "Good day!"

langue = input("Choisissez votre langue (FR ou EN) : ")

salutation = get_salutation(langue)
print(salutation)

def bienDit(word):
    if is_palindrome(word):
        return "Bien dit!"
    else:
        mirrored_text = word[::-1]
        return mirrored_text

while True:
    user_input = input("J'écoute ('exit' pour quitter) : ")

    if user_input.lower() == 'exit':
        auRevoir = get_salutation(langue)
        print(auRevoir)
        break

    bienDit(user_input)