#Converting String into list
name = "kiran raj r"
nameList = list(name)
print("String converted into list : ", nameList)

#converting a string into list using split
nameSplit = name.split()
print("List from split method ", nameSplit)

#Converting a string into list using split with delimiter
name1 = "kiran.raj.r"
nameSplitDelimit = name1.split('.')
print("List from split method using delimiter ",nameSplitDelimit)
print("After joining the list : "," ".join(nameSplitDelimit))