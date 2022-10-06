import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.ndimage import convolve
from urllib.request import urlopen
from matplotlib.pyplot import figure
import cv2

img_src = './data/'


def img_show(image, **argv):
    plt.figure(figsize=(30, 30))
    plt.imshow(image, **argv)  # display the image
    plt.axis('off')
    plt.show()
def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    return image
