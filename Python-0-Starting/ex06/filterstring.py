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

        obj = ft_filter(lambda S: len(S) > length, argv[0].split(" "))
        # lambda <var 1>, .., <var n> en parametre de la fonction : code
        # Ici return True si exp verifiee False sinon

        # Pas a la norme flake8:
        # x = lambda S: len(S) > length
        # obj = ft_filter(x, argv[0].split(" "))
        # Sans utiliser la fonction lambda :
        # def ft_check_length(S: str) -> bool:
        #     '''
        #     ft_check_length(S: str) -> bool.

        #     Return True if the length of str is higher than the number passed
        #     as the second argument of the program.
        #     Otherwise return False.
        #     '''
        #     if len(S) > length:
        #         return True
        #     return False
        # obj = ft_filter(ft_check_length, argv[0].split(" "))
        print(obj)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
