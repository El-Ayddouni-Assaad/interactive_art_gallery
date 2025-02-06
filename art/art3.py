import turtle
import random

def draw_spirals():
    screen = turtle.Screen()
    screen.title("Generative Art - Random Spirals")
    screen.bgcolor("black")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()

    for _ in range(36):
        artist.color(random.choice(["red", "blue", "green", "yellow", "purple", "white"]))
        for size in range(20, 200, 20):
            artist.circle(size)
            artist.right(10)

    screen.mainloop()

if __name__ == "__main__":
    draw_spirals()
