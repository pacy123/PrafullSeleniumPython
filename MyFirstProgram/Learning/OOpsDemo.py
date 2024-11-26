#Classes
#user define prototype
#blueprint  , sum, multiplication, addition
#methods, variables, instance variable, constructor

#self is required to call the class name
#Constructor name should be unique
#new keyword is not required

class Calculator:
    num = 100  # class variables
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("this is constructor")

        #in constructor is instance varable



    def getData(self):
        print("Now executing method in calss")


    def Summstion(self):
        return self.firstnumber+self.secondnumber+self.num



obj=Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.Summstion())

obj=Calculator(4,5)
obj.getData()
print(obj.num)
print(obj.Summstion())
#constructor in calss -   object with create directly


