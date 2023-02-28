class person(object):  #create a parentclass
    def __init__(self,name,id):  #function using init
        self.name=name           #self put in variable
        self.id=id               
    def display(self):              #create another function
        print(self.name,self.id)    

emp=person('satyam',102)  #calling the class by giving the value creation object
emp.display() #calling the function display

class emp(person):    #derivedclass(baseclass)
    def print(self):  #another function in print
        print('emp class called')
empdetails=emp('mayank',104)#giving value in emp creation object
empdetails.display()#calling display
empdetails.print()#calling print function