from abc import ABC, abstractmethod


# An Abstract Base Class (ABC) defines methods that must be implemented by its
# subclasses
class Character(ABC):
    """
    Your docstring for Class
    """
    @abstractmethod
    # Abstract methods are methods that are defined in an abstract class but
    # do not have an implementation. They serve as a blueprint for the
    # subclasses, ensuring that they provide their own implementation.
    def die(self):
        pass


class Stark(Character):
    """
    Your docstring for Class
    """
    first_name = ''
    is_alive = True

    def __init__(self, name: str):
        self.first_name = name
    
    def __init__(self, name: str, is_alive: bool):
        self.first_name = name
        self.is_alive = is_alive
    
    def die(self):
        self.is_alive = False
