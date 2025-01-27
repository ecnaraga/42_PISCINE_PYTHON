def ft_load_bar(p: float) -> str:
    '''
    ft_load_bar(p: float) -> str: return an array filled with the characters
        for the loading bar that represent the current progress
    p: float => percentage of load : from 0 to 1
    '''
    n = int(40 * p)
    array = ["█" for x in range(0, n)] + [" " for x in range(n, 40)]
    return "".join(array)


def ft_load_string(i: int, n: int) -> str:
    '''
    ft_load_string(i: int, n: int) -> str: return the string printed by tqdm
    i: int => value of the current progress
    n: int => value when 100% is reached
    '''
    s = ""
    p = i * 100 / n
    if p < 100:
        s += " "
    s += str(int(p)) + "%|" + ft_load_bar(i / n)
    s += "| " + str(i) + "/" + str(n)
    return s

# Marche mais le calcul des intervales impossible a faire sans time ne
# marcherait pas ici car on retourne une map avec tous les print
# + pas opti niveau memoire spatiale
# def ft_tqdm(lst: range) -> object:
#     '''
#     '''
#     return map((lambda x: print(f"\r{ft_load_string(x, lst.stop)}", end='')),
#        range(lst.start, lst.stop + 1))


# 1.Dans la vraie tqdm, l'utilisation de la bibli time permet de calculer
#   le temps depuis la premiere fois qu elle a ete appelee et donc d actualiser
#   l'affichage en fonction d'intervale et non systematiquement 1 par 1
# 2.Et pour que la barre soit "responsive" selon la largeur du terminal, il
#   faudrait utiliser la bibli shutil
# 3.Yield tranforme une fonction classique en generator
#   => Permet de renvoyer une valeur a l'appelant tout en sauvegardant son etat
#   => Quand la fonction sera rappelee, elle reprendra apres le yield la ou
#       elle s'est arretee
#   Ici yield exec printf et renvoie le retour de printf a chaque appel
def ft_tqdm(lst: range):
    '''
    ft_tqdm(lst: range): If called in a loop, print a progress bar
    take a range as parameter.
    Return each time a yield is reach and restart where it stopped at the
    previous call
    '''
    for i in range(0, lst.stop - lst.start + 1):
        yield print(f"\r{ft_load_string(i, lst.stop - lst.start)}", end='')
        i += 1
