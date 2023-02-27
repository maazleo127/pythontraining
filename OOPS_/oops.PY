class calculator:
    def add(self,a,b):
        print(a+b)        #without return
    
    def sub(self,a,b):   #these are called function,methods 
        return a-b
    @staticmethod
    def multi(a,b):
        return a*b
c=calculator()       #object which has class in it
# a=c.add(5,6)         #calling object and function
# b=c.sub(5,6)
d=c.multi(5,6)
c.add(6,11)         #without return
print(d)