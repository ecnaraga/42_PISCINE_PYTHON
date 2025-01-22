import sys

array = sys.argv
if len(array) < 2 :
    print("")
elif len(array) > 2 :
    print("AssertionError: more than one argument is provided")
else :
    try :
        a = int(array[1])
        if a % 2 == 0 :
            print("I'm Even.")
        else :
            print("I'm Odd.")
    except Exception as e :
        print("AssertionError: argument is not an integer")
