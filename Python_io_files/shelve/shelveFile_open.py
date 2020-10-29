import shelve
myShelveFile = shelve.open('myData')
print(myShelveFile['me'])