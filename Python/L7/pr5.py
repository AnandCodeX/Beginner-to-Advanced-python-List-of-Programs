#wamd to generate bill 
menu={'idli':20,'vada':30,'dosa':25}
amount=0.0
while True:
    op=int(input("1-add 2-amount 3-exit"))
    if op==1:
        item_name=input("Enter order")
        price=menu.get(item_name,-1)
        if price==-1:
            print("check food item name")
        else:
            qty=int(input("enter quantity order"))
            amount=amount+price*qty
            

    elif op==2:
        print("amount =",amount)
    elif op==3:
        break
    else:
        print("envalid option")    