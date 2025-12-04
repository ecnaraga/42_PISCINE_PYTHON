from S1E9 import Character

class Baratheon(Character):
    """
Subclass of the abstract class Character that represent a Baratheon Character.
    """

    def __init__(self, name: str, is_alive=True) -> None:
        """
Constructor of a Baratheon instance
:param self: Instance of the Baratheon class
:param name: Mandatory parameter
    => Instance variable => First name of the Baratheon
:type name: str
:param is_alive: Optional parameter set to True by default
    => Instance variable => Health state of the Baratheon
:type is_alive: bool
        """
        self.first_name = name
        self.is_alive = is_alive
        # # We could replace the two previous lines by calling the constructor
        # # inherited from the Character class :
        # super().__init__(name, is_alive)  # Call parent constructor
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
Docstring for __str__
:param self: Instance of the Baratheon class
:return: Information of family name, eyes colors, hairs colors
:rtype: str
        """
        return "('" + self.family_name + "', '" + self.eyes + "', '" + self.hairs + "')"

    def __repr__(self) -> str:
        """
Docstring for __repr__
:param self: Instance of the Baratheon class
:return: execution of __str__
:rtype: str
        """
        return "Vector: " + self.__str__()

    def die(self) -> None:
        """
def die(self) => Method that change to False the instance variable is_alive
:param self: Instance of the Baratheon class
        """
        self.is_alive = False


class Lannister(Character):
    """
Subclass of the abstract class Character that represent a Lannister Character.
    """

    def __init__(self, name: str, is_alive=True) -> None:
        """
Constructor of a Lannister instance
:param self: Instance of the Lannister class
:param name: Mandatory parameter
    => Instance variable => First name of the Lannister
:type name: str
:param is_alive: Optional parameter set to True by default
    => Instance variable => Health state of the Lannister
:type is_alive: bool
        """
        self.first_name = name
        self.is_alive = is_alive
        # # We could replace the two previous lines by calling the constructor
        # # inherited from the Character class :
        # super().__init__(name, is_alive)  # Call parent constructor
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
Docstring for __str__
:param self: Instance of the Lannister class
:return: Information of family name, eyes colors, hairs colors
:rtype: str
        """
        return "('" + self.family_name + "', '" + self.eyes + "', '" + self.hairs + "')"

    def __repr__(self) -> str:
        """
Docstring for __repr__
:param self: Instance of the Lannister class
:return: execution of __str__
:rtype: str
        """
        return "Vector: " + self.__str__()

    def die(self) -> None:
        """
def die(self) => Method that change to False the instance variable is_alive
:param self: Instance of the Lannister class
        """
        self.is_alive = False

    # method decorator => When a method has this decorator, it allow us to
    # wrap the code of the method called in a logic that would be coded each
    # time without the decorator and that can be the same for multiple methods
    def creation_character(func):
        """
Decorator function that call the method assorted with te decorator and
return its result
:param func: method that posses the decorator @creation_character
        """
        def wrapper(*args, **kwargs):
            """
Wrapper's decorator of @creation_character
            """
            # Can do something before
            res = func(*args, **kwargs)
            # Can do something after
            return res
        return wrapper

    @creation_character
    def create_lannister(name: str, is_alive=True) -> object:
        """
Method that return a new instance of Lannister
:param name: Mandatory parameter
    => Instance variable => First name of the Lannister
:type name: str
:param is_alive: Optional parameter set to True by default
    => Instance variable => Health state of the Lannister
:type is_alive: bool
        """
        return (Lannister(name, is_alive))
