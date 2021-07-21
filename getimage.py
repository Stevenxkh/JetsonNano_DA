from urllib.request import urlretrieve
import signal
import sys, argparse
import os
import cv2
import time

parser=argparse.ArgumentParser()

parser.add_argument('--url', default = 'http://114.32.238.30:8083/video1s2.mjpg' , help='fetch url')
parser.add_argument('--path', default = 'img' , help='img save path')

args=parser.parse_args()

os.system("mkdir "+args.path)

for i in range(2400):
    cap = cv2.VideoCapture(args.url)#get rtsp stream(.mjpg)
    ret, frame = cap.read()
    for k in range(30):
        cap.read()
    outpath = args.path + '/' + str(i) + '.jpg'
    if ret == True:
        cv2.imwrite(outpath, frame)
        print(outpath+' save!')


'''
for i in range(1):

    if args.url == None:
        url = 'http://114.32.238.30:8083/video1s2.mjpg'
    else:
        url = args.url

    outpath = out_folder + '/' + str(i) + '.jpg'

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(60)
    try:
        urlretrieve(url, outpath)
    except Exception as e:
        print(e)
        print(outpath+' save!')
'''
#this function is for request timeout
def handler(signum, frame):
   raise Exception("timeout!")
