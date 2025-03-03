import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    '''
    def give_bmi(
        height: list[int | float], weight: list[int | float]
    ) -> list[int | float]:
    GOAL
        Create and return a list of the BMI (Body Mass Index) calculating from
            the lists of weight and height
    MATH formula : BMI = weight / height^2
    '''
    if len(height) is not len(weight):
        raise Exception("Assertion error: Both list should have the same type")
    if not all(type(w) is float or type(w) is int for w in weight):
        raise Exception(
            "Assertion error: Weight list should contain only int or float")
    if not all(type(h) is float or type(h) is int for h in height):
        raise Exception(
            "Assertion error: Height list should contain only int or float")
    return (np.array(weight) / (np.array(height) * np.array(height))).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    GOAL :
        Create an return a list of booleans take True if BMI is above the limit
            else False
    '''
    if not all(type(x) is float or type(x) is int for x in bmi):
        raise Exception(
            "Assertion error: Bmi list should contain only int or float")
    if type(limit) is not int:
        raise Exception("Assertion error: Limit should be an int")
    limits = [True if x > limit else False for x in bmi]
    return limits

# np.array() => transform an object into an array that allow us to do array
#   operations => ex :
#   listA = [1, 2, 3]
#   listB = [4, 5, 6]
#   Impossible to do listA + listB If we want to add list A[0] to listB[0],...
#   np.array(listA) = [1 2 3]
#   np.array(listA) + np.array(listB) = [1+4 2+5 3+6]
