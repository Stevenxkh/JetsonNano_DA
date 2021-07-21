import config
import mse
import RTSP_get_stream as rtsp
import time

print(config.ODF_info)

rtsp.get_frame(config.ODF_info['target_0'])
rtsp.get_frame(config.ODF_info['target_1'])

path = config.ODF_info['path']
print(mse.init_cmp(path + '/' + config.ODF_info['target_0'], path + '/' + config.ODF_info['target_1']))
