import turtle as t

# Set up the Turtle screen
screen = t.Screen()
screen.bgcolor("white")

# Create a Turtle object for drawing
cat_face = t.Turtle()
cat_face.speed(1)  # Set the drawing speed

# Draw the cat's head
cat_face.penup()
cat_face.goto(0, -100)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("gray")
cat_face.circle(100)
cat_face.end_fill()

# Draw the left eye
cat_face.penup()
cat_face.goto(-30, 30)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("white")
cat_face.circle(30)
cat_face.end_fill()

# Draw the right eye
cat_face.penup()
cat_face.goto(30, 30)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("white")
cat_face.circle(30)
cat_face.end_fill()

# Draw the pupils
cat_face.penup()
cat_face.goto(-20, 40)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("black")
cat_face.circle(10)
cat_face.end_fill()

cat_face.penup()
cat_face.goto(20, 40)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("black")
cat_face.circle(10)
cat_face.end_fill()

# Draw the nose
cat_face.penup()
cat_face.goto(0, 10)
cat_face.pendown()
cat_face.begin_fill()
cat_face.fillcolor("pink")
cat_face.circle(15)
cat_face.end_fill()

# Draw the mouth
cat_face.penup()
cat_face.goto(0, 10)
cat_face.pendown()
cat_face.setheading(-60)
cat_face.circle(20, 120)

# Hide the Turtle and display the cat face
cat_face.hideturtle()
t.done()

# Close the window on click
screen.exitonclick()
