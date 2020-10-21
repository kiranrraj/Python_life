import shelve

shelveFile = shelve.open('myData')
shelveFile['me'] = {
    'name': 'kiran raj r',
    'place' : 'Trivandrum'
}

shelveFile.close()