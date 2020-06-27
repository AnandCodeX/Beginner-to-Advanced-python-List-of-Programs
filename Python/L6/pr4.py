#wapf my range() to which we can passs 1 arg and 2 argument

def my_range(n1=None,n2=None):
    if n1 is not None and n2 is None:
        start=1
        while start<=n1:
            print(start)
            start=start+1

    elif n1 is not None and n2 is not None:
        start = n1
        while start <= n2:
            print(start)
            start=start+1

my_range(3,9)


