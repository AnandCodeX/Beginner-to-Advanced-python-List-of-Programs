#wapp to delete file

import os.path
filename=input("enter file name")
if os.path.exists(filename):
    os.remove(filename)
    print(filename,"file deleted")
else:
    print(filename,"does not exist")
