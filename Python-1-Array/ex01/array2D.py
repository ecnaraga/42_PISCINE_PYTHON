import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    def slice_me(family: list, start: int, end: int) -> list:
    Return a version of family reshaped :
        - start indicates the index of the first element
        - end indicates the index where to stop adding elements
    '''
    if type(family) is not list or not all(
        type(elem) is list for elem in family
    ):
        raise Exception(
            "Assertion error: Family should be a list of lists")
    if not all(len(elem) is len(family[0]) for elem in family):
        raise Exception(
            "Assertion error: All list in family should have the same size")
    if type(start) is not int or type(end) is not int:
        raise Exception(
            "Assertion error: Start and End index should be int")
    print("My shape is ", np.shape(family))
    family = family[start:end]
    print("My new shape is ", np.shape(family))
    return family
