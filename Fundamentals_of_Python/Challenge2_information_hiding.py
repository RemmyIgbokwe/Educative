class Student:
    def setName(self, name): 
        self.__name = name
        #self.__rollnumber = rollnumber
        #pass

    def getName(self):
        return self.__name
        #pass

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
        #self.__rollnumber = y
        #pass

    def getRollNumber(self):
        return self.__rollNumber
        #pass
    


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())