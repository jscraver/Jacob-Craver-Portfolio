######################################################################################################################
# Name: Jaocb Craver
# Date: 03/18/20
# Description: Points Program
######################################################################################################################

# the 2D point class
class Point(object):

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
    # getter for x coordinate
    @property
    def x(self):
        return float(self._x)

    #setter for x coordinate
    @x.setter
    def x(self, value):
        self._x = value

    # getter for y coordinate
    @property
    def y(self):
        return float(self._y)

    # setter for y coordinate
    @y.setter
    def y(self, value):
        self._y = value

    # magic function to return x and y coordinates as an ordered pair 
    def __str__(self):
        return("({},{})".format(self.x, self.y))

    # function to calculate the distance between two points
    def dist(self, other):
        deltaX = self.x - other.x
        deltaY = self.y - other.y
        return(deltaX**2 + deltaY**2)**0.5
        
    # function to calculate the midpoint between two points
    def midpt(self, other):
        midX = (self.x + other.x)/2
        midY = (self.y + other.y)/2
        return(Point(midX, midY))
        
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print ("p1:", p1)
print ("p2:", p2)
print ("p3:", p3)
# calculate and display some distances
print ("distance from p1 to p2:", p1.dist(p2))
print ("distance from p2 to p3:", p2.dist(p3))
print ("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print ("midpt of p1 and p2:", p1.midpt(p2))
print ("midpt of p2 and p3:", p2.midpt(p3))
print ("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print ("p4:", p4)
print ("distance from p4 to p1:", p4.dist(p1))
