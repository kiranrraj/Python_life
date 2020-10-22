import traceback 

try:
    raise Exception('This is the error message')
except:
    errFile = open('errfile.txt', 'w')
    errFile.write(traceback.format_exc())
    errFile.close()

    print(f"Error msg has been written to errfile.txt")