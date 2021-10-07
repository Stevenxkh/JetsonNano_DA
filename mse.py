#import skimage.measure
#from skimage.metrics import structural_similarity as ssim
#from skimage import measure
import numpy as np
import cv2
#import config


def mse(imageA, imageB, threshold):
    '''
    the 'Mean Squared Error' between the two images is
    the sum of the squared difference between the two images;
    '''
    mse_sum = 0
    pixel_num = 0
    # NOTE: the two images must have the same dimension

    for i in range(imageA.shape[0]):
        for j in range(imageA.shape[1]):
            tmp = abs(imageA[i][j] - imageB[i][j])
            if tmp > threshold :
                mse_sum += (tmp ** 2)
                pixel_num += 1


    #err = np.sum((imageA - imageB) ** 2) ** 2
    #print(err)
    #err /= (imageA.shape[0] * imageA.shape[1])
    err = mse_sum/pixel_num
    print(mse_sum, pixel_num)
    '''
    return the MSE, the lower the error, the more "similar" the two images are
    '''
    return err

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity index for the images
    m = mse(imageA, imageB ,50)
    # s = ssim(imageA, imageB)
    return m


def init_cmp(imageA_path, imageB_path):

    # read image by cv2 from path
    target_0 = cv2.imread(imageA_path)
    target_1 = cv2.imread(imageB_path)

    # convert image to grayscale
    target_0 = cv2.cvtColor(target_0, cv2.COLOR_BGR2GRAY)
    target_1 = cv2.cvtColor(target_1, cv2.COLOR_BGR2GRAY)

    return compare_images(target_0, target_1)
