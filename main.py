from_latin_to_morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    "¿": "..-.-",
    "¡": "--...-",
    " ": " "
}

from_morse_to_latin_alphabet = {v: k for k, v in from_latin_to_morse_alphabet.items()}
print(from_morse_to_latin_alphabet)


def toMorse(latin_string):
    morse_string = ""
    for letter in latin_string:
        morse_letter = from_latin_to_morse_alphabet.get(f"{letter.capitalize()}")
        morse_string = morse_string + morse_letter + " "

    return morse_string


def toString(morse_string):
    latin_string = ""
    morse_symbol = ""
    spaces = 0

    for letter in morse_string:

        # Construct the symbol as long as no space in encountered
        if letter != " ":
            morse_symbol += letter
            spaces = 0

        # Spaces Management
        elif letter == " ":
            spaces += 1

            # First space equals end of morse symbol => Appends latin letter to the latin string
            if spaces == 1:
                if morse_symbol != "":
                    latin_letter = from_morse_to_latin_alphabet.get(morse_symbol)
                    latin_string += str(latin_letter)
                    morse_symbol = ""

            # Second spaces and above == real spaces
            elif spaces >= 2:
                latin_string = latin_string + " "

    # Gets last letter in the latin string
    if morse_symbol != "":
        latin_letter = from_morse_to_latin_alphabet.get(morse_symbol)
        latin_string = latin_string + latin_letter

    return latin_string


print("--- Welcome to the Morse Code Converter ---\n\n")

translation_on = "y"
while translation_on == "y":
    translation_type = ""
    while translation_type != "morse to string" and translation_type != "string to morse":
        translation_type = input(
            "Type 'morse to string' or 'string to morse' to select your translation type: ").lower()

    user_input = input("Please provide a string: ")

    if translation_type == "morse to string":
        print(f"Translated into Latin: {toString(user_input)} \n\n")
    else:
        print(f"Translated into Morse: {toMorse(user_input)} \n\n")

    translation_on = input("Continue ? (Y/N)").lower()
