def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
        print('now i wanf tro introduce some heroes')
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

har=['harry','rohan','skillf','hammad']
normal='i am normal arguments'
kw={'rohan':'monitor','harry':'fitness instructor','the programmer':'coordinator'}
funargs(normal,*har,**kw)