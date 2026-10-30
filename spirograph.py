import turtle
import colorsys

# Set up the drawing screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Creative Python Spirograph")

# Create the artist turtle
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.width(2)

# Number of shapes to draw in the loop
total_shapes = 60

# Draw the geometric pattern
for i in range(total_shapes):
    # Calculate a smooth rainbow color transition
    hue = i / total_shapes
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    artist.color(color)
    
    # Draw a circle with a shifting angle
    artist.circle(100)
    artist.left(360 / total_shapes)

# Keep the window open when finished
artist.hideturtle()
screen.mainloop()
