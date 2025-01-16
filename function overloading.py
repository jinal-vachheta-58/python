class Surface_Area:
    def calculate_area(self, radius=None, length=None, width=None, height=None, base=None):
        if radius is not None:
           #return self.calculate_area_circle(radius)
            return 3.14 * radius * radius
           
        elif length is not None and width is not None:
           # return self.calculate_area_rectangle(length, width)
            return length * width
        elif height is not None and base is not None:
           # return self.calculate_area_triangle(height, base)
            return 0.5 * height * base
        else:
            print("Invalid input")



surface_area = Surface_Area()

while True:
    print("1. Calculate area of Circle")
    print("2. Calculate area of Rectangle")
    print("3. Calculate area of Triangle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", surface_area.calculate_area(radius=radius))
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle   : "))
        print("Area of the rectangle:", surface_area.calculate_area(length=length, width=width))
    elif choice == 3:
        height = float(input("Enter the height of the triangle: "))
        base = float(input("Enter the base of the triangle: "))
        print("Area of the triangle:", surface_area.calculate_area(height=height, base=base))
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
