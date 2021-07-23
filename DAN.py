import requests, time, csmapi, random
 
profile = {
    'd_name': None,
    'dm_name': 'MorSensor',
    #'u_name': 'yb',
    'is_sim': False,
    'df_list': ['Acceleration', 'Temperature'],
}
mac_addr = 'C860008BD249'

def get_mac_addr():
    from uuid import getnode
    mac = getnode()
    mac = ''.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac

timestamp={}
MAC=get_mac_addr()
thx=None
def register_device(addr):
    global MAC, profile, timestamp, thx
    if csmapi.ENDPOINT == None: print ('Server url is empty.')
    if addr != None: MAC = addr
    if profile['d_name'] == None: profile['d_name']= str(int(random.uniform(1, 100)))+'.'+ profile['dm_name']
    for i in profile['df_list']: timestamp[i] = ''
    print('IoTtalk Server = {}'.format(csmapi.ENDPOINT))
    if csmapi.register(MAC,profile):
        print ('This device has successfully registered.')
        print ('Device name = ' + profile['d_name'])
        return True
    else:
        print ('Registration failed.')
        return False

def device_registration_with_retry(URL=None, addr=None):
    if URL != None:
        csmapi.ENDPOINT = URL
    success = False
    while not success:
        try:
            register_device(addr)
            success = True
        except Exception as e:
            print ('Attach failed: '),
            print (e)
        time.sleep(1)

def pull(FEATURE_NAME):
    global timestamp
    data = csmapi.pull(MAC,FEATURE_NAME)
        
    if data != []:
        if timestamp[FEATURE_NAME] == data[0][0]:
            return None
        timestamp[FEATURE_NAME] = data[0][0]
        if data[0][1] != []:
            return data[0][1]
        else: return None
    else:
        return None

def push(FEATURE_NAME, *data):
    return csmapi.push(MAC, FEATURE_NAME, list(data))

def get_alias(FEATURE_NAME):
    try:
        alias = csmapi.get_alias(MAC,FEATURE_NAME)
    except Exception as e:
        return None
    else:
        return alias

def set_alias(FEATURE_NAME, alias):
    try:
        alias = csmapi.set_alias(MAC, FEATURE_NAME, alias)
    except Exception as e:
        return None
    else:
        return alias
		
def deregister():
    return csmapi.deregister(MAC)
