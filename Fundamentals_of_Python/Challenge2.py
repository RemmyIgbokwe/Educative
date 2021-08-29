from typing import TextIO


class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy 
        self.chem = chem
        self.bio = bio
        #pass

    def totalObtained(self):
        total = self.phy + self.chem + self.bio
        return total
        #pass

    def percentage(self):
        percentage = ((self.totalObtained())/300) * 100
        return percentage
        #pass

grades = Student("Remmy", 75, 50, 90)
print(grades.percentage())
print(grades.name)