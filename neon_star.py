import turtle
import colorsys

# Set up the drawing screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Matrix")

artist = turtle.Turtle()
artist.speed(0)
artist.width(1)

# Draw an expanding, colorful neon web
for i in range(180):
    hue = i / 180
    color = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    artist.color(color)
    
    # Move forward an increasing distance, then make a sharp turn
    artist.forward(i * 2)
    artist.left(145)

artist.hideturtle()
screen.mainloop()
