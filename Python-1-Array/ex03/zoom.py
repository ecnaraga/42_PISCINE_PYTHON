from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''
    '''
    array = ft_load("images/animal.jpeg")
    print(array)
    array = array[100:500, 462:862, 0:1]  # Slice image from row 100 to 500, from col 462 to 862, keep first byte for the color 
    print("New shape after slicing:", np.shape(array))
    print(array)
    plt.imshow(array, cmap='gray')  # 
    plt.show()


if __name__ == "__main__":
    main()
