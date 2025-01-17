# List : indexed by a range of numbers
ft_list = ["Hello", "tata!"]
# Tuple(2 elements) or n-uplet : Equivalent NON MODIFIABLE aux listes
    # => Une fois defini, le tuple est imuable
    # => Si 3 elements ex 1, 2, 3 ou (1, 2, 3) => Triplet 
ft_tuple = ("Hello", "toto!")
# Ensemble: Un ensemble est une collection non ordonnée sans éléments en
#   double. Un ensemble permet de réaliser des tests d'appartenance ou des
#   suppressions de doublons de manière simple. Les ensembles savent
#   également effectuer les opérations mathématiques telles que les unions,
#   intersections, différences et différences symétriques.
ft_set = {"Hello", "tutu!"}
# Dictionary : indexed by keys => Hello is the key for titi
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World"

ft_tuple = "Hello", "France"
# or :
# ft_tuple = ("Hello", "France")

ft_set.discard("tutu!")
# or
# ft_set.remove("tutu!")
ft_set.add("Paris")

ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)