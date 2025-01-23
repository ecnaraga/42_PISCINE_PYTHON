import sys


class Morse:
    '''
    Attributs :
        NESTED_MORSE: Dictionary with all the symbol translate in morse
        s : String to convert in morse
    Fuction :
        __init__(self, s: str) : Constructor with a string in parameter
        morse_print(self) -> None:
    '''
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "-.... ",
    }

    def __init__(self, s: str):
        '''
        __init__(self, s: str):
        Constructor with a string as parameter
        If a char is not alphanumeric or a space raise an exception
        Otherwise stock the string in UPPERCASE
        '''
        for c in s:
            if not c.isalnum() and c != " ":
                raise "AssertionError"
        self.s = s.upper()

    def morse_print(self) -> None:
        '''
        Morse_class.morse_print(self) -> None:
        Print in morse code the string stocked in s
        '''
        for x in self.s:
            print(self.NESTED_MORSE[x], end="")
        print("")


def main():
    '''
    Take a string as argument, encode it to morse code, and print it.
    The string can contain only alphanumeric characters or spaces.
    '''
    try:
        if len(sys.argv) != 2:
            raise "AssertionError"
        s = sys.argv[1]
        morse = Morse(s)
        morse.morse_print()
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
