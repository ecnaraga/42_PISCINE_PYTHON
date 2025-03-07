from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def slice_array(array: np.array) -> np.array:
    '''
    def slice_array(array: np.array) -> np.array:
    Slice image from row 100 to 500, from col 462 to 862, keep 1st byte
        for the shape of gray and return array
    '''
    array = array[100:500, 462:862, 0:1]
    print("New shape after slicing:", np.shape(array))
    print(array)
    return array


def transpose_array(array: np.array) -> np.array:
    '''
    def transpose_array(array: np.array) -> np.array:
        Return array with axes of X and Y swapped
    '''
    # Avec numpy lib :
    # array = np.swapaxes(array, 0, 1).reshape(400, 400)
    # array = np.transpose(array).reshape(400, 400)
    for i in range(0, 400):
        for j in range(i, 400):
            tmp = array[i][j][0]
            array[i][j][0] = array[j][i][0]
            array[j][i][0] = tmp
    return array


def main():
    '''
    '''
    array = ft_load("images/animal.jpeg")
    if array is None:
        return
    print(array)
    try:
        array = slice_array(array)
        array = transpose_array(array).reshape(400, 400)  # Voir avec quelqu un si reshape ici c est ok pour rester sur un np.array
        print(np.shape(array))
        print(array)
        # Display data as an image 2D + set colormapping with cmap, vmin, vmax:
        plt.imshow(array, cmap='gray', vmin=0, vmax=255)
        plt.show()  # Display all open figure
    except Exception as e:
        print("Error :", e)


if __name__ == "__main__":
    main()
