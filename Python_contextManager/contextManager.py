from contextlib import contextmanager
import os

@contextmanager
def chage_directory(dest):
    try:
        cwd = os.getcwd();
        os.chdir(dest)
        yield
    finally:
        os.chdir(cwd)

with chage_directory('D:\gitHub\Python_life'):
    print(os.listdir())