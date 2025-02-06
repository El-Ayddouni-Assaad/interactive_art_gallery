import turtle
import random
import sys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("the shapes project")
artist = turtle.Turtle()
artist.speed(10)
artist.hideturtle()

class shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        print(f"drawing a shape at ({self.x},{self.y}) with color {self.color}")

class circle(shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def animation(self):
        artist.penup()
        artist.goto(self.x, self.y)
        artist.color(self.color)
        artist.pendown()
        artist.circle(self.radius)

    def draw(self):
        print(f"drawing a circle at ({self.x},{self.y}) with color {self.color} and radius {self.radius}")

class rectangle(shape):
    def __init__(self, x, y, color, L, l):
        super().__init__(x, y, color)
        self.L = L
        self.l = l

    def animation(self):
        artist.penup()
        artist.goto(self.x, self.y)
        artist.color(self.color)
        artist.pendown()
        for _ in range(2):
            artist.forward(self.L)
            artist.left(90)
            artist.forward(self.l)
            artist.left(90)

    def draw(self):
        print(f"drawing a rectangle at ({self.x},{self.y}) with color {self.color} and a length and width ({self.L},{self.l})")

class triangle(shape):
    def __init__(self, x, y, color, L, h):
        super().__init__(x, y, color)
        self.L = L
        self.h = h

    def animation(self):
        artist.penup()
        artist.goto(self.x, self.y)
        artist.color(self.color)
        artist.pendown()
        for _ in range(3):
            artist.forward(self.L)
            artist.left(120)

    def draw(self):
        print(f"drawing a triangle at ({self.x},{self.y}) with color {self.color} with a base and height ({self.L},{self.h})")

def draw_shape(color, shape_type):
    if(shape_type=="random"):
        shape_type=random.choice(["square","triangle","circle"])
        if(color=="random"):
            color=random.choice(["red","green","blue","yellow","purple","orange"])
            if shape_type == "circle":
                my_circle = circle(0, -200, color, 200)
                my_circle.animation()
            elif shape_type == "triangle":
                my_triangle = triangle(0, 0, color, 200, 2)
                my_triangle.animation()
            elif shape_type == "square":
                my_rectangle = rectangle(0, 0, color, 200, 200)
                my_rectangle.animation()
        else:
            if shape_type == "circle":
                my_circle = circle(0, -200, color, 200)
                my_circle.animation()
            elif shape_type == "triangle":
                my_triangle = triangle(0, 0, color, 200, 2)
                my_triangle.animation()
            elif shape_type == "square":
                my_rectangle = rectangle(0, 0, color, 200, 200)
                my_rectangle.animation()
    else:
        if(color=="random"):
            color=random.choice(["red","green","blue","yellow","purple","orange"])
            if shape_type == "circle":
                my_circle = circle(0, -200, color, 200)
                my_circle.animation()
            elif shape_type == "triangle":
                my_triangle = triangle(0, 0, color, 200, 2)
                my_triangle.animation()
            elif shape_type == "square":
                my_rectangle = rectangle(0, 0, color, 200, 200)
                my_rectangle.animation()
        else:
            if shape_type == "circle":
                my_circle = circle(0, -200, color, 200)
                my_circle.animation()
            elif shape_type == "triangle":
                my_triangle = triangle(0, 0, color, 200, 2)
                my_triangle.animation()
            elif shape_type == "square":
                my_rectangle = rectangle(0, 0, color, 200, 200)
                my_rectangle.animation()
    screen.mainloop()

if __name__ == "__main__":
    user_color = sys.argv[1] if len(sys.argv) > 1 else "white"
    user_shape = sys.argv[2] if len(sys.argv) > 2 else "circle"
    draw_shape(user_color, user_shape)
