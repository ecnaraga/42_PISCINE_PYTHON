from time import strftime, localtime, time
from datetime import timedelta
 
time_curr = time()
print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation" .format(time_curr))
print(strftime("%b %d %Y", localtime()))

# Cours format dans print :
# {0:,.4f} => le 0 devant le ":" represente l index de l argument a recuperer passe dans la fonction format() soit on va formatter time_curr
#         => , dit d'utiliser une virgule comme separateur de millier => Attention a l'ordre!!
#         => .4 donne la precision : 4 chiffre apres la virgule
#         => f pour nombre flottant
# {0:.2e} => .2 donne la precision : 2 chiffre apres la virgule
#         => e pour ecriture scientific

## Pour limiter la partie decimal d un nombre flottant (f) a 4 chiffres :
# print("%.4f}" % time_curr)
## or : 
# print("{0:.4f}".format(time_curr))
## or :
# print(round(time_curr, 4))

# Sources :
# - https://docs.python.org/fr/3.13/library/time.html#time.strptime
# - https://www.w3schools.com/python/ref_string_format.asp
# - https://realpython.com/python-string-formatting/#using-strformat-to-format-strings