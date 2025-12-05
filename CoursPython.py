# 1.LIST/ARRAY MANIPULATION:          https://www.datacamp.com/tutorial/python-slice?utm_cid=19589720821&utm_aid=157156375191&utm_campaign=230119_1-ps-other~dsa~tofu_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9198704-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~emea-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=19589720821&gclid=CjwKCAiA3L_JBhAlEiwAlcWO59jsjOxOp5qX3ch7eJmU9ojj6DEdxMR--KO4KilIU-G9rzfqb7EhuBoCmlIQAvD_BwE

ma_liste = [1, 2, 3, 4, 5]
ma_liste[1] # => premier element
ma_liste[-1] # => dernier element
ma_liste[1:] # => tous sauf le premier element
ma_liste[:-1] # => tous sauf le dernier element
ma_liste[::-1] # => inverse la liste (premier element devient le dernier, ...)
ma_liste[::2] # => 1 element sur 2 en commencant a l index 0 (maliste devient [1, 3, 5])
ma_liste = ma_liste[:2] ou ma_liste = ma_liste[0:2] # => ma_liste ne contient plus que les 2 premiers elements
ma_liste = ma_liste[1:3] # => ma_liste ne contient plus que les elements 2 et 3 indexe [1] et [2]

################################################################################

# 2.SYNTAX :

(x[-1] == "K" or x[-1] == "k") # equivalent to : x[-1] in "Kk"

################################################################################

# 3.COMPREHENSION LIST:

# [expression for item in iterable if condition]
# a.

            #########################

# b. Multiple item in multiple iterable:
V3 = [x + y for x in V1 for y in V2]

# Equivalent a:
i = 0
for x in V1:
    for y in V2:
        V3[i] = x + y
        i += 1

V3 = [x + y for x, y in zip(V1, V2)]

# Equivalent a:
i = 0
for x, y in zip(V1, V2):
    V3[i] = x + y
    i += 1

################################################################################

# 4.LAMBDA FUNCTIONS:

# a.
lambda x: float(x[:-1]) if x[-1] == "M" else (float(x[:-1])*0.001 if (x[-1] == "K" or x[-1] == "k") else float(x)*0.000001)


# Equivalent a:


def function(x: str) -> float:
    if x[-1] == "M":
        x = float(x[:-1])
    elif x[-1] == "K" or x[-1] == "k":
        x = float(x[:-1])*0.001
    else:
        x = float(x)*0.000001
    return x

            #########################

# b.
lambda x, y: x + y


# Equivalent a:


def function(x: str, y: str) -> str:
    return x + y

################################################################################

# 5.DECORATOR
def my_decorator(func):
    """
Decorator function that call the method assorted with te decorator and
return its result
:param func: method that posses the decorator @my_decorator
    """
    def wrapper(*args, **kwargs):
        """
Wrapper's decorator of @my_decorator
        """
        # Code that will be executed BEFORE the execution of the func assorted with the decorator
        res = func(*args, **kwargs)
        # Code that will be executed AFTER the execution of the func assorted with the decorator
        return res
    return wrapper
