import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        # Draw the trunk
        t.forward(branch_length)
        
        # Draw the right subtree
        t.right(20)
        draw_tree(branch_length - 15, t)
        
        # Draw the left subtree
        t.left(40)
        draw_tree(branch_length - 15, t)
        
        # Return to the original position
        t.right(20)
        t.backward(branch_length)

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
tree_turtle = turtle.Turtle()
tree_turtle.speed(0)  # Set the drawing speed (0 is fastest)

# Set the initial position and direction
tree_turtle.left(90)
tree_turtle.up()
tree_turtle.backward(100)
tree_turtle.down()

# Call the draw_tree function to draw the tree
draw_tree(100, tree_turtle)

# Close the window on click
screen.exitonclick()
