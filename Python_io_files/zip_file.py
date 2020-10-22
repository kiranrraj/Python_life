import zipfile, os

zipFileObj = zipfile.ZipFile('example.zip')
fileDetails = zipFileObj.namelist()
print(fileDetails)

new_details = zipFileObj.getinfo('new.txt')
print(f"Details about new.txt  {new_details}")
print(f"Details about net.txt actual size {new_details.file_size}")
print(f"Details about compressed size {new_details.compress_size}")

# zipFileObj.extractall() #To extract all the files in zipfile 

zipFileObj.close()
