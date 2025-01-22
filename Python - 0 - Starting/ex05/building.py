import sys

def print_type_character(str: str) -> None :
    '''
    Print the total number of characters and of each type of character.
    
    Arguments :
        str (str) : String.
    
    Return :
        None.
    '''
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0
    for c in str :
        if c.isdigit() :
            digit += 1
        elif c.islower() :
            lower += 1
        elif c.isupper() :
            upper += 1
        elif c.isspace() :
            space += 1
        elif c.isprintable() :
            punct += 1
    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")

def main() :
    '''
    Call print_type_character

    Argument :
        string
    
    Return :
        None
    '''
    try :
        # help(print_type_character)
        # print(print_type_character.__doc__)
        if len(sys.argv) > 2 :
            print("AssertionError: more than one argument is provided")
            return
        if len(sys.argv) == 1 :
            str = input("What is the text to count?\n")
        else :
            str = sys.argv[1]
        print_type_character(str)
    except Exception as e :
        return
if __name__ == "__main__":
    main()

# Pour le test avec /r : python building.py $'Hello\rWorld'
