#from urllib.request import urlretrieve
import cv2
import os
import config

def get_frame(f_name):

    # get rtsp stream(.mjpg)
    try:
        cap = cv2.VideoCapture(config.ODF_info['url'])
    except Exception as e:
        print(e)
    # read the next frame of rtsp stream
    ret, frame = cap.read()

    # make the path to save frame(image)
    os.system("mkdir " + config.ODF_info['path'])
    outpath = config.ODF_info['path'] + '/' + str(f_name)

    # check if stream has been read
    if ret == True:
        cv2.imwrite(outpath, frame)
        print(outpath+' save!')
