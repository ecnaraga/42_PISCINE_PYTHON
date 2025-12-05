class calculator:
    """
Class that allow to do calculations of vector with a scalar
    """
    def __init__(self, lhs):
        """
Constructor

:param self:  Instance of the class
:param lhs: Vector on which the calculation will be executed
        """
        self.val = lhs

    def __add__(self, object: int | float) -> None:
        """
Addition of a vector with a scalar
:param self: Instance of the class
:param object: Scalar to add to the vector
:type object: int | float
        """
        self.val = [x + object for x in self.val]
        print(self.val)

    def __mul__(self, object: int | float) -> None:
        """
Multiplication of a vector with a scalar
:param self: Instance of the class
:param object: Scalar multiplier
:type object: int | float
        """
        self.val = [x * object for x in self.val]
        print(self.val)

    def __sub__(self, object: int | float) -> None:
        """
Subtraction of a vector with a scalar
:param self: Instance of the class
:param object: Scalar to subtract to the vector
:type object: int | float
        """
        self.val = [x - object for x in self.val]
        print(self.val)

    def __truediv__(self, object: int | float) -> None:
        """
Division of a vector with a scalar
:param self: Instance of the class
:param object: Scalar divisor
:type object: int | float
        """
        try:
            self.val = [x / object for x in self.val]
            print(self.val)
        except Exception as e:
            print("AssertionError:", e)
