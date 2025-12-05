class calculator:
    """
Class that allow to do calculations of 2 vectors
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
Docstring for Dot product
Formula : Dot product = V1[0] * V2[0] + V1[1] * V[1] + ... + V1[n] * V2[n]
:type V1: list[float]
:param V2: Second vector
:type V2: list[float]
        """
        V1 = [x * y for x, y in zip(V1, V2)]
        dot = 0
        for i in range(len(V1)):
            dot += V1[i]
        print("Dot product is :", dot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
Addition of 2 vectors
:param V1: First vector
:type V1: list[float]
:param V2: Second vector
:type V2: list[float]
        """
        # The zip() function returns a zip object, which is an iterator of
        # tuples that allow us to iterate on the same time on the 2 vectors
        V1 = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is :", [f"{n:.1f}" for n in V1])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
Subtraction of 2 vectors
:param V1: First vector
:type V1: list[float]
:param V2: Second vector
:type V2: list[float]
        """
        V1 = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is :", [f"{n:.1f}" for n in V1])
