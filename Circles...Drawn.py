######################################################################################################################
# Name: Jacob Craver
# Date: 03/30/20
# Description: Circles...Drawn Program
######################################################################################################################
from tkinter import *
from random import randint, choice
# the Circle class. All circles have an x and y coordinate for their
# centers, a rad value for their radius, and a color.
class Circle(object):
    
    def __init__(self, x = 0.0, y = 0.0, radius = 0.0, color = "black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
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

    # getter for radius
    @property
    def radius(self):
        return float(self._radius)
    # setter for radius
    @radius.setter
    def radius(self, value):
        if (value < 0.0):
            self._radius = self.radius
        else:
            self._radius = value

    # getter for color
    @property
    def color(self):
        return self._color
    # setter for color
    @color.setter
    def color(self, value):
        self._color = value

    # magic function return (x, y, radius, color)
    def __str__(self):
        return("({}, {}, {}, {})".format(self.x, self.y, self.radius, self.color))

    # function to calculate the distance between two points
    def dist(self, other):
        deltaX = self.x - other.x
        deltaY = self.y - other.y
        return(deltaX**2 + deltaY**2)**0.5
                 
# the Diagram class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class Diagram(Canvas):
    # class variables for max circle radius and colors
    max_circle_radius = 5
    colors = "black", "red", "green", "blue", "cyan", "yellow", "magenta"
    
    def __init__(self, master):
        Canvas.__init__(self, master)
        self.pack(fill = BOTH, expand = 1)

    # function that draws circles using instances of the Circle class
    def drawCircles(self, n):
        for i in range(n):
            circle = Circle(randint(0, WIDTH-1), randint(0, HEIGHT-1), randint(0, Diagram.max_circle_radius), choice(Diagram.colors))
            self.create_oval(circle.x, circle.y, circle.x+circle.radius*2, circle.y+circle.radius*2, outline = circle.color, fill = circle.color)
             

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of circles to draw
NUM_CIRCLES = 500

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Circles...drawn")
# create the Diagram as a Tkinter canvas inside the window
s = Diagram(window)
# draw some random circles
s.drawCircles(NUM_CIRCLES)
# wait for the window to close
window.mainloop()
