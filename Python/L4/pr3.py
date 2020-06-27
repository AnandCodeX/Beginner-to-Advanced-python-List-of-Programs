#wapp to 
import array
stack =array.array('i',[])

while True:
    op=int(input("1 push, 2 pop, 3 peek 4 display 5 exit"))

    if op == 1:
        ele=int(input("enter data to push "))
        stack.append(ele)
        print(ele,"is pushed on the stack")
    elif op==2:
        if len(stack)==0:
            print("stack is empty")
        else:
            ele=stack[-1]
            print("popped element is ",ele)
    elif op==3:
        if len(stack)==0:
            print("stack is empty")
        else:
            ele = stack[-1]
            print("topmost element is", ele)
    elif op==4:
        if len(stack)==0:
            print("stack is empty")
        else:
            print(stack)
    elif op==5:
        break
    else:
        print("invalid option")
