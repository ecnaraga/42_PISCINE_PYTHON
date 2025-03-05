from PIL import Image
import numpy as np


# def ft_load(path: str) -> array:
def ft_load(path: str) -> np.array:
    '''
    def ft_load(path: str) -> np.array
    Print the shape of the image and return the array of the image
    '''
    if type(path) is not str:
        print("Assertion Error : Argument expected is a string")
        return
    try:
        image = Image.open(path)
        array = np.asarray(image)
        image.close()
        print("The shape of the image is :", np.shape(array))
        return array
    except OSError:
        print("Assertion Error : Non valid path")
