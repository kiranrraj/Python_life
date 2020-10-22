import time, logging
logging.basicConfig(filename="traffic_light_log.txt" ,level=logging.DEBUG,
                        format= '%(asctime)s -- %(levelname)s -- %(message)s')
light = {
    'ns' : 'green',
    'ew' : 'red'
}


def switchLights(lt):
    loop = 0
    for key in lt.keys():
        loop+=1
        logging.debug(f"Loop {loop} starts -- Directory: {light[key]}, key : {key}")
        if lt[key] == 'green':
            lt[key] = 'yellow'
        elif lt[key] == 'yellow':
            lt[key] = 'red'
        elif lt[key] == 'red':
            lt[key] = 'green'
        logging.debug(f"Loop {loop} ends -- Directory: {light[key]}, key: {key}")
        
    try:
        assert 'red' in lt.values(), 'Neither light is red ' + str(lt)
    except : 
        logging.error(f"Exception occured : ", exc_info=True)
    return lt[key]

print(f"The current status of traffic light {switchLights(light)}")
time.sleep(1)
print(f"The current status of traffic light {switchLights(light)}")
time.sleep(1)
print(f"The current status of traffic light {switchLights(light)}")