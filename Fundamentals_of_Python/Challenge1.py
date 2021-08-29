class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        total = (self.x **2) + (self.y **2) + (self.z **2)
        return total

mynum = Point(4, 5, 6)        
print(mynum.sqSum())