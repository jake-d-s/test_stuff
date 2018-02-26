

def morse_translate(input_string):
    morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                  "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                  "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                  "y": "-.--", "z": "--.."}
    new_text = ""
    for char in input_string:
        if char.isalpha():
            new_text += morse_dict[char.lower()] + " "
        elif char == " ":
            new_text += "  "
        elif char in ["?", ".", "!"]:
            new_text += morse_translate("  stop ")
        else:
            new_text += char

    return new_text

def main(input_string=None):
    if input_string is None:
        input_string = input("What string do you want to translate?\n>>> ")

    return morse_translate(input_string)

if __name__ == "__main__":
    text = ("Python has some string methods that will evaluate to a Boolean value. These methods are useful when we are " +
            "creating forms for users to fill in, for example. If we are asking for a post code we will only want to " +
            "accept a numeric string, but when we are asking for a name, we will only want to accept an alphabetic string.\n")

    print(main("."))
