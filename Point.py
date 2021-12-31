# Point object in two-dimensions
# Attributes x, y
# Methods, getX, getY, Distance, setX, setY, __repr__(), __init__()
import math

class Point(object):
    def __init__(self, x, y):
        if not isinstance(x, (float, int)):
            raise ValueError("UPS! ... x-coordinate must be float or int")
        if not isinstance(y, (float, int)):
            raise ValueError("UPS! ... y-coordinate must be float or int")
        self.Y = y
        self.X = x

    def __repr__(self):
        return "({0},{1})".format(self.X, self.Y)

    # Accessors or Getter methods
    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    # Mutators or Setter methods
    def setX(self, newx):
        self.X = newx

    def setY(self, newy):
        self.Y = newy

    def distance(self, aPoint):
        #return ((self.X - aPoint.X)**2 + (self.Y - aPoint.Y)**2) ** (1/2)
        return math.sqrt(math.pow(self.X - aPoint.X, 2) + math.pow(self.Y - aPoint.Y, 2))


if __name__ == "__main__":
    point1 = Point(0, 0)
    print(point1)

    point2 = Point(-1, -3)
    print(point2, point2.X, point2.Y)

    #point3 = Point("hello", "world")
    #print(point3)

    print(point1.getX() == 0)   # expected output is 0
    print(point1.getY())

    point2.setX(5)
    print(point2.getX() == 5)

    d = point1.distance(point2)
    print(d)   # check by hand that the result is indeed correct