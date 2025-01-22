# shapes.py

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

def generate_shapes(shape_type, **kwargs):
    """
    Function to generate shape objects.
    
    shape_type: str (e.g., 'circle' or 'rectangle')
    kwargs: parameters for the shape (e.g., radius, length, width)
    
    Returns:
        An object of the requested shape class.
    """
    if shape_type.lower() == 'circle':
        return Circle(kwargs['radius'])
    elif shape_type.lower() == 'rectangle':
        return Rectangle(kwargs['length'], kwargs['width'])
    else:
        raise ValueError("Unsupported shape type. Choose 'circle' or 'rectangle'.")