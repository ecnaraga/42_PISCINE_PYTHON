# filter.__doc__ :
# 'filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which
# function(item)\nis true. If function is None, return the items
# that are true.'

def ft_filter(f, objs: any) -> list:
    '''
    ft_filter(f, objs: any) -> list:
    Apply to an object a function and return with all the elements that match.

    Arguments:
        1. Function that take one parameter of the type stored in the object
        and return a boolean.
        2. Object.

    Return:
        Object of the same type than the one in argument.
    '''
    objs = [x for x in objs if f(x)]

    return objs
