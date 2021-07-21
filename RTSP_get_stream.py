from urllib.request import urlretrieve
import cv2
import os
import config

def get_frame(f_name):
    cap = cv2.VideoCapture(config.ODF_info['url'])#get rtsp stream(.mjpg)
    ret, frame = cap.read()

    os.system("mkdir " + config.ODF_info['path'])
    outpath = config.ODF_info['path'] + '/' + str(f_name)
    if ret == True:
        cv2.imwrite(outpath, frame)
        print(outpath+' save!')
