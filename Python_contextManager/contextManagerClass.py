import os

class contextMan:
    def __init__(self, dest):
        self.dest = dest
    
    def __enter__(self):
        self.cwd = os.getcwd()
        os.chdir(self.dest)
    
    def __exit__(self, exec_type, exe_val, traceback):
        os.chdir(self.cwd)

with contextMan('D:/gitHub/Python_life'):
    print(os.listdir())

with contextMan('D:/gitHub'):
    print(os.listdir())