from abc import ABC, abstractmethod


# An Abstract Base Class (ABC) defines methods that must be implemented by its
# subclasses
class Character(ABC):
    """
Abstract Class that requires in its subclasses the following methods:
- def die(self)
    """

    def __init__(self, name: str, is_alive=True):
        """
def __init__(self) => Constructor of a Character instance
:param self: Instance of the Character class
:param name: Mandatory parameter
    => Instance variable => First name of the Character
:type name: str
:param is_alive: Optional parameter set to True by default
    => Instance variable => Health state of the Character
:type is_alive: bool
        """
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    # Abstract methods are methods that are defined in an abstract class but
    # do not have an implementation. They serve as a blueprint for the
    # subclasses, ensuring that they provide their own implementation.
    def die(self):
        pass


class Stark(Character):
    """
Subclass of the abstract class Character that represent a Stark Character.
    """

    def die(self):
        """
def die(self) => Method that change to False the instance variable is_alive
:param self: Instance of the Stark class
        """
        self.is_alive = False
