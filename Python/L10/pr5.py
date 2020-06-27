#wapp to create file if file doess not exist file name would be supplied by the user

import os.path
filename=input("enter file name")
if os.path.exists(filename):
    print(filename,"already exist")
else:
    f=None
    try:
        f=open(filename,"a")
        print(filename,"created")

    
    except Exception as e:
        print("issue",e)
    finally:
        if f is not None:
            f.close()