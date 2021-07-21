#import skimage.measure
from skimage.metrics import structural_similarity as ssim
# from skimage import measure
import numpy as np
import cv2
import config


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    return m, s


def init_cmp(imageA, imageB):
    print(imageA,imageB)
    target_0 = cv2.imread(imageA)
    target_1 = cv2.imread(imageB)
    target_0 = cv2.cvtColor(target_0, cv2.COLOR_BGR2GRAY)
    target_1 = cv2.cvtColor(target_1, cv2.COLOR_BGR2GRAY)
    return compare_images(target_0, target_1)
