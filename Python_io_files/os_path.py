import os

my_path = 'D:\gitHub\Python_life\Python_io_files\os_path.py'

joined_path = os.path.join('c', 'user', 'kiran')
print(joined_path)

pwd = os.getcwd()
print(f"The current working directory : {pwd}")

# os.chdir('D:\gitHub\Python_life')
# pwd = os.getcwd()
# print(pwd)

absolute_path = os.path.abspath('os_path.py')
print(f"Absolute path of 'os_path.py' is : {absolute_path}")

print(f"Absolute path of '.' is : {os.path.abspath('.')}")
print(os.path.isabs(my_path))

relative_path = os.path.relpath(my_path)
print(f"Relative path of '{my_path}' : {relative_path}")

base_name = os.path.basename(my_path)
print(f"Base path of {my_path} is {base_name}")

dir_name = os.path.dirname(my_path)
print(f"Base path of {my_path} is {dir_name}")

print(f"Path split {os.path.split(my_path)}")
print(f"Path seperator {os.path.sep}")
print(f"Path split using path seperator{my_path.split(os.path.sep)}")
