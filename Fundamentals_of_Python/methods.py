class Player:

    LastName = "Igbokwe"

    def __init__(self, name): 
        self.__name = name 
    
    def demo(self):
        return self.__name

    @classmethod
    def demo2(cls, othername):
        return cls.LastName +" "+ othername 

    @staticmethod 
    def demo3(a,b):
        result = a*b
        print(f"The answer is: {result} for {a} * {b}" )    
        #print("The answer is: {} for {} * {}".format(result, 3, 2) )    


p1 = Player("smart")
# print(p1.demo())
# print(p1.demo2("Mira"))
print(p1.demo3(2,3))
p1.name = "King"
print(p1.name)