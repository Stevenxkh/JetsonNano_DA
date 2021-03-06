import config
import mse
import RTSP_get_stream as rtsp
import time
import requests

#sent signal to IotTalk to turn on the light
r = requests.put(config.ODF_info['RC_url_0'], json={"data": [1]})

#wait for light ready(20sec)
print("sending signal to turn on light...")
time.sleep(20)

# get IPCam image through rtsp request
for i in range(10):
    rtsp.get_frame(str(i) + ".jpg")

path = config.ODF_info['path']


# compute avg mse between every image(no spray)
N_spray_sum = 0
for i in range(0,10):
    for k in range(0,10):
        if(i != k):
            m = mse.init_cmp(path + '/' + str(i) + ".jpg", path + '/' + str(k) + ".jpg")
            #print("mse: " + str(m))
            N_spray_sum += m

print("avg mse: " + str(float(N_spray_sum)/90))


#sent signal to IotTalk to open the spray
#r = requests.put(config.ODF_info['RC_url_1'], json={"data": [1]})
r = requests.put(config.ODF_info['RC_url_0'], json={"data": [0]})
print("sending signal to turn on spray...")


#wait for spray ready(20sec)
time.sleep(20)

# get IPCam image through rtsp request
for i in range(10,20):
    rtsp.get_frame(str(i) + ".jpg")

#r = requests.put(config.ODF_info['RC_url_1'], json={"data": [0]})
print("sending signal to turn off spray and light...")

#sent signal to IotTalk to turn off the light
#r = requests.put(config.ODF_info['RC_url_0'], json={"data": [0]})


# compute avg mse between every image(spray)
Spray_sum = 0
for i in range(10,20):
    for k in range(10,20):
        if(i != k):
            m = mse.init_cmp(path + '/' + str(i) + ".jpg", path + '/' + str(k) + ".jpg")
            #print("mse: " + str(m))
            Spray_sum += m

print("avg mse: " + str(float(Spray_sum)/90))

# compute avg mse between every image(spray v.s. no spray)
cmp_sum = 0
for i in range(10):
    for k in range(10,20):
        if(i != k):
            m = mse.init_cmp(path + '/' + str(i) + ".jpg", path + '/' + str(k) + ".jpg")
            #print("mse: " + str(m))
            cmp_sum += m

print("avg mse: " + str(float(cmp_sum)/100))
diff_mse = float(cmp_sum)/100

"""
/* TODO */
compute MSE to tell user DEVICE work or not
"""

if diff_mse > 8000:
    print("device work correct!")
else:
    print("there are some trouble...")
