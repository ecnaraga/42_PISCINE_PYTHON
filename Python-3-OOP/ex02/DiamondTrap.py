from S1E7 import Baratheon, Lannister


# The Diamond Problem occurs in multiple inheritance scenarios where ambiguity
# arises in method resolution. Python's MRO (method resolution order), based
# on the C3 Linearization Algorithm, elegantly resolves this issue:
# MRO ensures that methods are resolved in a predictable and consistent order,
# eliminating ambiguity and duplication.
# The MRO rules are:
# - Parents classes are called from left to right
# - Common classes are called just once
# Can do class.mro() to check the order
class King(Baratheon, Lannister):
    """
Subclass of the abstracts class Baratheon and Lannister that represent a King
Character.
    """

    def set_eyes(self, color: str):
        """
Attribute a eye color
:param self: Instance of the King class
:param color: Define the new color
:type color: str
        """
        self.eyes = color

    def set_hairs(self, color: str):
        """
Attribute a hair color
:param self: Instance of the King class
:param color: Define the new color
:type color: str
        """
        self.hairs = color

    def get_eyes(self) -> str:
        """
Get the eye color
:param self: Instance of the King class
:return: return the color
:rtype: str
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
Get the hairs color
:param self: Instance of the King class
:return: return the color
:rtype: str
        """
        return self.hairs
