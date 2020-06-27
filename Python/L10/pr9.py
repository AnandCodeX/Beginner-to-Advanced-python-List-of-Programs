#wapp to read data from file if it exist

import os.path
filename=input("enter file name")
if os.path.isfile(filename):
    with open(filename) as f:
       data=f.read()
       print(data)
else:
    print("file does not find")