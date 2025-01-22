import sys
from ft_filter import ft_filter


def main():
    '''
    Print the list of words of a string S which length isn\'t higher than a
    number N:
    S -> str : First argument represent a string.
    N -> str : Second argument represent a integer.
    '''
    try:
        if len(sys.argv) != 3:
            raise
        argv = [sys.argv[i] for i in range(1, 3)]
        length = int(argv[1])

        def ft_check_length(S: str) -> bool:
            '''
            ft_check_length(S: str) -> bool.

            Return True if the length of str is higher than the number passed
            as the second argument of the program.
            Else return False.
            '''
            if len(S) > length:
                return True
            return False

        obj = ft_filter(ft_check_length, argv[0].split(" "))
        print(obj)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
