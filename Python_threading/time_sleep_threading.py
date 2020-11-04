# Using the threading
# Author : Kiran raj r

import threading
import time

print("Start of program")


def greet():
    time.sleep(5)
    print("Hello world")


threadObj = threading.Thread(target=greet)
threadObj.start()


def greetMe(name):
    time.sleep(5)
    print(f"Hello {name}")


threadObj = threading.Thread(target=greetMe, args=['kiran'])
threadObj.start()

print("Program ends")
