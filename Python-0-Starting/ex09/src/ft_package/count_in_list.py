def count_in_list(args: list, s: any) -> int:
    '''
    Return the numbers of occurrences of s in args
    '''
    i = 0

    for arg in args:
        if arg == s:
            i += 1
    return i
