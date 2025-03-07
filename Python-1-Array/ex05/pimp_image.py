import numpy as np  # Lib to manipulate table
import matplotlib.pyplot as plt  # Lib to display image
from skimage.color import rgb2gray  # Lib to manipulate image


def ft_invert(array: np.array) -> np.array:
    '''
def ft_invert(array: np.array) -> np.array:
Invert the color of the image received
    '''
    array2 = array.copy()
    for row in array2:
        for col in row:
            for i in range(3):
                col[i] = 255 - col[i]
    plt.imshow(array2)
    plt.axis('off')  # Say to not display axis
    plt.show()
    return array2


def ft_red(array: np.array) -> np.array:
    '''
def ft_red(array: np.array) -> np.array:
Apply filter red to the image received
    '''
    array2 = array.copy()
    for row in array2:
        for col in row:
            for i in range(1, 3):
                col[i] *= 0
    plt.imshow(array2)
    plt.axis('off')
    plt.show()
    return array2


def ft_green(array: np.array) -> np.array:
    '''
def ft_green(array: np.array) -> np.array:
Apply filter green to the image received
    '''
    array2 = array.copy()
    for row in array2:
        for col in row:
            col[0] -= col[0]
            col[2] -= col[2]
    plt.imshow(array2)
    plt.axis('off')
    plt.show()
    return array2


def ft_blue(array: np.array) -> np.array:
    '''
def ft_blue(array: np.array) -> np.array:
Apply filter blue to the image received
    '''
    array2 = array.copy()
    for row in array2:
        for col in row:
            for i in range(0, 2):
                col[i] = 0
    plt.imshow(array2)
    plt.axis('off')
    plt.show()
    return array2


def ft_grey(array: np.array) -> np.array:
    '''
def ft_gray(array: np.array) -> np.array:
Apply filter gray to the image received
    '''
    array2 = array.copy()
    # for row in array2:
    #     for col in row:
    #         col[0] = 0.299 * col[0] + 0.587 * col[1] + 0.114 * col[2]
    #         col[1] = col[0]
    #         col[2] = col[0]
    grayscale = rgb2gray(array2)
    plt.imshow(grayscale, cmap=plt.cm.gray)
    plt.axis('off')
    plt.show()  # Display all open figure
