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
    #tmp_k = np.zeros((imageA.shape[0], imageA.shape[1]))
    #print(tmp_k)
    for i in range(imageA.shape[0]):
        for j in range(imageA.shape[1]):

            tmp = int(imageA[i][j]) - int(imageB[i][j])
            if tmp > threshold:
                #tmp_k[i][j] = (tmp ** 2)
                mse_sum += (tmp ** 2)
                pixel_num += 1




    #err1 = np.sum(tmp_k)

    err = mse_sum/pixel_num
    print("cmp: ")
    #print("A-B\n", cv2.subtract(imageB, imageA), "\n\n", "manual minus\n", tmp_k)
    #print("\n\n")
    #print("A\n", imageA, "\n\n", "B\n", imageB)
    print(err)


    '''
    return the MSE, the lower the error, the more "similar" the two images are
    '''
    #return 0
    return err

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity index for the images
    m = mse(imageA, imageB ,10)
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
