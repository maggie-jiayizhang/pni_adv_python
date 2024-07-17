import matplotlib.pyplot as plt

# show a matrix as a grayscale image
def show_grayscale(img, ax=None):
    if (ax is None):
        _, ax = plt.subplots(1, 1)
    ax.imshow(img, cmap='gray')