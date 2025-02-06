import turtle
import random
import sys

def draw_random_circles(color, shape):
    screen = turtle.Screen()
    screen.title("Generative Art - Random Circles")
    screen.bgcolor("white")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()
    colors=["red","green","blue","yellow","purple","orange"]
    if(color=="random"):
        for _ in range(50):
            artist.penup()
            color=random.choice(colors)
            artist.color(color)
            artist.goto(random.randint(-300, 300), random.randint(-300, 300))
            artist.pendown()
            if shape == "circle":
                artist.circle(random.randint(20, 100))
            elif shape == "square":
                for _ in range(4):
                    artist.forward(40)
                    artist.right(90)
            elif shape == "triangle":
                for _ in range(3):
                    artist.forward(40)
                    artist.left(120)
            elif shape == "random":
                side=random.randint(3,8)
                for i in range (side):
                    artist.forward(40)
                    artist.left(360/side)
    else :
        for _ in range(50):
            artist.penup()
            artist.color(color)
            artist.goto(random.randint(-300, 300), random.randint(-300, 300))
            artist.pendown()
            if shape == "circle":
                artist.circle(random.randint(20, 100))
            elif shape == "square":
                for _ in range(4):
                    artist.forward(40)
                    artist.right(90)
            elif shape == "triangle":
                for _ in range(3):
                    artist.forward(40)
                    artist.left(120)
            elif shape == "random":
                side=random.randint(3,8)
                for i in range (side):
                    artist.forward(40)
                    artist.left(360/side)
    screen.mainloop()

if __name__ == "__main__":
    user_color = sys.argv[1] if len(sys.argv) > 1 else "white"
    user_shape = sys.argv[2] if len(sys.argv) > 2 else "circle"
    draw_random_circles(user_color, user_shape)
