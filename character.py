import turtle as t

# Set up the Turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a Turtle object for drawing
character = t.Turtle()
character.speed(1)  # Set the drawing speed

# Draw a yellow filled circle for the face
character.begin_fill()
character.fillcolor("yellow")
character.circle(100)
character.end_fill()

# Draw the left eye
character.penup()
character.goto(-40, 120)
character.pendown()
character.begin_fill()
character.fillcolor("white")
character.circle(25)
character.end_fill()

# Draw the right eye
character.penup()
character.goto(40, 120)
character.pendown()
character.begin_fill()
character.fillcolor("white")
character.circle(25)
character.end_fill()

# Draw the smile
character.penup()
character.goto(0, 50)
character.pendown()
character.setheading(-60)
character.circle(80, 120)

# Hide the Turtle and display the character
character.hideturtle()
t.done()

# Close the window on click
screen.exitonclick()
