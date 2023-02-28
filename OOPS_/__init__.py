class person:
    def __init__(self,name):       #selfname is defined in init function and
        self.name=name                

    def say_hi(self):
        print('hello,my name is :',self.name)    #when we call the say_hi function 
p=person('nikhil') #passing in class value and calling sayhi with p gives 
p.say_hi()             #value of init without mentioning init 