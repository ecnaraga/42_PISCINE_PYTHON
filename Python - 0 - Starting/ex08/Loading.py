def ft_load_stringg(p: float) -> str:
    n = int(40 * p)
    array = ["█" for x in range(0, n)] + [" " for x in range(n, 40)]
    return "".join(array)


def ft_load_string(i: int, n: int) -> str:
    s = ""
    p = i * 100 / n
    if p < 100:
        s += " "
    s += str(int(p)) + "%|" + ft_load_stringg(i / n)
    s += "| " + str(i) + "/" + str(n)
    return s


def ft_tqdm(lst: range) -> object:
    '''
    '''
    # lst = range(lst.start, lst.stop + 1)
    # print(type(lst))
    return map((lambda x: print(f"\r{ft_load_string(x, lst.stop)}", end='')), range(lst.start, lst.stop + 1))
    # return map((lambda x: print(f"{int(x / 333 * 100)}%|{ft_load_stringg(x / 333)}| {x}/333", end='\r')), lst)
