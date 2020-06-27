#wapp to write into file

import os.path
filename=input("enter file name")
if os.path.isfile(filename):
    f=None
    try:
        f=open(filename,"a")
        data=input("enter data = ")
        f.write(data+"\n")
        print("work done")
    except Exception as e:
        print("issue", e)
    finally:
        if f is not None:
            f.close()
else:
    print("file does not exist")
