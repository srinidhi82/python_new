 #Import the shapes module
from shape import generate_shapes

# Generate a Circle object
circle = generate_shapes('circle', radius=5)

# Generate a Rectangle object
rectangle1 = generate_shapes('rectangle', length=10, width=4)

# Use the objects
print("Circle:")
print(f" - Radius: {circle.radius}")
print(f" - Area: {circle.area()}")
print(f" - Perimeter: {circle.perimeter()}")

print("\nRectangle:")
print(f" - Length: {rectangle1.length}")
print(f" - Width: {rectangle1.width}")
print(f" - Area: {rectangle1.area()}")
print(f" - Perimeter: {rectangle1.perimeter()}")