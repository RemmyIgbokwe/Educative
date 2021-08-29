class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        #pass

    def add(self):
        return(self.num1+self.num2)
        #pass

    def subtract(self):
        return(self.num2-self.num1)
        #pass

    def multiply(self):
        return(self.num1*self.num2)
        #pass

    def divide(self):
        return(self.num2/self.num1)
        #pass

find = Calculator(5,4) 
print(find.add())
print(find.subtract())
print(find.multiply())
print(find.divide())


