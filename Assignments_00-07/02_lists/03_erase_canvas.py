import turtle

# Canvas ki size aur cells ki details
canvas_width = 500
canvas_height = 500
num_cols = 25
num_rows = 25
cell_width = canvas_width // num_cols
cell_height = canvas_height // num_rows
eraser_size = 20  # Eraser ka size

# Turtle object banate hain drawing ke liye
screen = turtle.Screen()
screen.setup(width=canvas_width, height=canvas_height)
screen.bgcolor("white")  # Canvas ka background white
screen.tracer(0)  # Animation ko fast karta hai
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Grid banate hain blue cells ke saath
def draw_grid():
    for row in range(num_rows):
        for col in range(num_cols):
            x = -canvas_width / 2 + col * cell_width
            y = canvas_height / 2 - row * cell_height
            pen.goto(x, y)
            pen.pendown()
            pen.fillcolor("blue")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(cell_width)
                pen.right(90)
            pen.end_fill()
            pen.penup()
    screen.update()

# Eraser ka function
eraser = turtle.Turtle()
eraser.shape("square")
eraser.shapesize(eraser_size / 20)  # Turtle size ko eraser size se adjust karte hain
eraser.fillcolor("white")
eraser.penup()
eraser.speed(0)

cells = {}  # Dictionary to keep track of cell colors
erasing = False  # To check if the mouse button is pressed

def erase(x, y):
    if not erasing:  # Only erase if the mouse button is pressed
        return
    eraser.goto(x, y)
    # Calculate the cell coordinates that the eraser is over
    min_x = int((x + canvas_width / 2 - eraser_size / 2) // cell_width)
    max_x = int((x + canvas_width / 2 + eraser_size / 2) // cell_width)
    min_y = int((canvas_height / 2 - y - eraser_size / 2) // cell_height)
    max_y = int((canvas_height / 2 - y + eraser_size / 2) // cell_height)

    for col in range(max(0, min_x), min(num_cols, max_x + 1)):
        for row in range(max(0, min_y), min(num_rows, max_y + 1)):
            cell_key = (row, col)
            if cells.get(cell_key, True):  # Only erase if the cell is not already erased
                x_cell = -canvas_width / 2 + col * cell_width
                y_cell = canvas_height / 2 - row * cell_height
                pen.goto(x_cell, y_cell)
                pen.pendown()
                pen.fillcolor("white")
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(cell_width)
                    pen.right(90)
                pen.end_fill()
                pen.penup()
                cells[cell_key] = False  # Mark the cell as erased
    screen.update()


# Mouse click handler to start erasing
def start_erase(x, y):
    global erasing
    erasing = True
    erase(x, y)


# Mouse button release handler to stop erasing
def stop_erase(x, y):
    global erasing
    erasing = False
    erase(x, y) # Erase one last time when the button is released


# Function to handle mouse movement (this will be called by the screen)
def move_eraser(x, y):
    if erasing:  # Only erase if the mouse button is pressed
        erase(x, y)

# Draw the initial grid
draw_grid()

# Set up event listeners for mouse dragging.  We use the basic onclick, and then use the turtle's
#  on drag functionality.
screen.listen()
screen.onscreenclick(start_erase, 1)  # 1 for left mouse button
screen.onscreenclick(stop_erase, 3)  # 3 for right mouse button (to stop erasing)
eraser.ondrag(move_eraser) # When the eraser is dragged, call the function.

screen.mainloop()  # Keep the window open
