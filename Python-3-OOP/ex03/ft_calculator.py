class calculator:
    """
    Docstring for calculator
    """
    def __init__(self, lhs):
        self.val = lhs
    
    def __add__(self, object: int | float) -> None:
        self.val = [x + object for x in self.val]
        print(self.val)
            
    def __mul__(self, object: int | float) -> None:
        self.val = [x * object for x in self.val]
        print(self.val)

    def __sub__(self, object: int | float) -> None:
        self.val = [x - object for x in self.val]
        print(self.val)

    def __truediv__(self, object: int | float) -> None:
        try:
            self.val = [x / object for x in self.val]
            print(self.val)
        except Exception as e:
            print("AssertionError:", e)
