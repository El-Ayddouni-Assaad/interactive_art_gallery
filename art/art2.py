import turtle
import random
import sys

def draw_grid(color, shape):
    screen = turtle.Screen()
    screen.title("Generative Art - Geometric Grid")
    screen.bgcolor("white")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()
    colors=["red","green","blue","yellow","purple","orange"]
    if(color=="random"):
        for y in range(-250, 250, 50):
            for x in range(-350, 350, 50):
                artist.penup()
                artist.goto(x, y)
                artist.pendown()
                color=random.choice(colors)
                artist.color(color)
                if shape == "square":
                    for _ in range(4):
                        artist.forward(40)
                        artist.right(90)
                elif shape == "circle":
                    artist.circle(20)
                elif shape == "triangle":
                    for _ in range(3):
                        artist.forward(40)
                        artist.left(120)
                elif shape== "random":
                    side=random.randint(3,8)
                    for _ in range(side):
                        artist.forward(40)
                        artist.left(360/side)
    else:
        for y in range(-250, 250, 50):
            for x in range(-350, 350, 50):
                artist.penup()
                artist.goto(x, y)
                artist.pendown()
                artist.color(color)
                if shape == "square":
                    for _ in range(4):
                        artist.forward(40)
                        artist.right(90)
                elif shape == "circle":
                    artist.circle(20)
                elif shape == "triangle":
                    for _ in range(3):
                        artist.forward(40)
                        artist.left(120)
                elif shape== "random":
                    side=random.randint(3,8)
                    for _ in range(side):
                        artist.forward(40)
                        artist.left(360/side)
    screen.mainloop()

if __name__ == "__main__":
    user_color = sys.argv[1] if len(sys.argv) > 1 else "white"
    user_shape = sys.argv[2] if len(sys.argv) > 2 else "square"
    draw_grid(user_color, user_shape)
