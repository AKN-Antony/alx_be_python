import math

class Shape:
    """Base class representing a geometric shape"""
    def area(self):
        """Calculate the area of the shape"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class representing a rectangle"""
    def __init__(self, length, width):
        """Initialize rectangle with length and width"""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate rectangle area (length × width)"""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle"""
    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius
    
    def area(self):
        """Calculate circle area (π × radius²)"""
        return math.pi * (self.radius ** 2)


# The main.py script would be used as provided in the task description
# Here's what it would look like for reference:
"""
from polymorphism_demo import Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
"""