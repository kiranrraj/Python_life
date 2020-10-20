import math

class Point:
    """A class to calculate the distance between two points"""

    def __init__(self, x, y):
        """Initialize a point"""
        self.move(x,y)

    def move(self, x, y):
        """Move a point to a new location"""
        self.x = x
        self.y = y

    def reset(self):
        """Move a point back to start"""
        self.move(0,0)
    
    def cal_distance(self, other_point):
        """Calculate distance between two points"""
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

point1 = Point(3,4)
point2 = Point(8,8)


print(point1.cal_distance(point2))