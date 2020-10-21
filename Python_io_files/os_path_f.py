import os

my_path = 'D:\gitHub\Python_life\Python_io_files\os_path_f.py'
size = os.path.getsize(my_path)
print(f"File size : {size}")

list_files = os.listdir(os.path.dirname(my_path))
print(f"Directory : {list_files}")

for fName, subF, fileN in os.walk('D:\gitHub\Python_life\Python_io_files'):
    print(f" {fName} : {subF} : {fileN}")