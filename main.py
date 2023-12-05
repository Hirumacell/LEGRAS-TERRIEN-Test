def is_palindrome(word):
    return word == word[::-1]

print("Hello mec!")

while True:
    user_input = input("J'écoute ('exit' pour quitter) : ")

    if user_input.lower() == 'exit':
        print("Slt!")
        break

    if is_palindrome(user_input):
        print("Bien dit!")
    else:
        mirrored_text = user_input[::-1]
        print(f"{mirrored_text}")
