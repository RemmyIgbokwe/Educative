class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        #pass

    def area(self):
        return ( self.__length * self.__width)
        #pass

    def perimeter(self):
        return (2*(self.__length + self.__width))
        #pass


shape1 = Rectangle(10, 3)
print(shape1.area())
print(shape1.perimeter())