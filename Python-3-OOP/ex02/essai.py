class shape:
    def greet(self):
        print("class shape called")

class circle(shape):
    def greet(self):
        super().greet()
        print("class circle called")

class square(shape):
    def greet(self):
        super().greet()
        print("class square called")

class cylinder(circle, square):
    def greet(self):
        super().greet()
        print("class cylinder called")

d = cylinder()
d.greet()