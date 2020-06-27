#wapp to write into file by WITH function

import os.path
filename=input("enter file name")
if os.path.isfile(filename):
    with open(filename,"a") as f:
        data=input("enter data = ")
        f.write(data+"\n")
        print("work done")
    
else:
    print("file does not exist")
