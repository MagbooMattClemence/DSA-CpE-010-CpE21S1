class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def display_area(self):
        print(f"The area of the rectangle is: {self.area()} square units")


# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Creating an instance of Rectangle
rect = Rectangle(length, width)

# Displaying the area
rect.display_area()
