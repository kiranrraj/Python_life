# Using the time.sleep() method
# Author : Kiran raj r

import datetime
import time


for i in range(60):
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    time.sleep(1)
