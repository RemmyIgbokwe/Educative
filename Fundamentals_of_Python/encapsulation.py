
class Player1: 
    __lastName = "Igbokwe"

    def __init__(self, firstName, height): 
        self.__firstName = firstName
        self.__height = height


    @staticmethod
    def getHeight(height1):
        return height1     
    
    @staticmethod
    def setHeight( height1, newHeight):
        Player1.getHeight(height1)
        height1 = newHeight
    
    @staticmethod
    def getFirstName(firstName): 
        return firstName

    staticmethod
    def setFirstName( newFirstName): 
         
        firstName = newFirstName

    @classmethod
    def setlastName(cls, newlastName):
        cls.__lastName = newlastName

    @classmethod
    def getlastName(cls):
        return cls.__lastName     



p2 = Player1("Emeka", "5.0")
p1 = Player1("smart", "6'3")
# print(p1.getlastName())
# p1.setlastName("Okafor")
# print(p1.getlastName())
print(p1.getHeight("6'3"))
# print(p1.getFirstName())
# p1.setFirstName("King", )
Player1.setHeight("6'3", "6'2")
print(p1.getHeight())
# print(p1.getFirstName())
# print(p2.getlastName())
