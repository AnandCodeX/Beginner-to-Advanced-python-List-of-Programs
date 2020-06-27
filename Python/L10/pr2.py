#wapp to access command line argument and recive two int and perform ans = n1/n2
#INPUT AT COMMAND LINE ONLY

import sys
try:
    n1=int(sys.argv[1])
    n2=int(sys.argv[2])
   
except(ValueError,IndexError,ZeroDivisionError):
    print("bad input enetr non zero and integrs only")
except Exception as e:
    print("some other issue",e)
else:    
    ans=n1/n2
    print("ans = ",ans)
finally:
    print("mission over")
