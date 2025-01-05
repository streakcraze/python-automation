import tkinter as tk

selected_shape = "square"
selected_color = "red"


def draw_shape(canvas, selected_shape=selected_shape, selected_color=selected_color):
    # Clear only the shapes, not the entire canvas
    for item in canvas.find_withtag("shape"):
        canvas.delete(item)
    x, y = 300, 200  # Constant location
    if selected_shape == "square":
        canvas.create_rectangle(x-20, y-20, x+20, y+20, fill=selected_color, tags="shape")
    elif selected_shape == "circle":
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=selected_color, tags="shape")
    elif selected_shape == "triangle":
        canvas.create_polygon(x, y-20, x-20, y+20, x+20, y+20, fill=selected_color, tags="shape")
    canvas.update()  # Ensure the canvas is updated


def select_shape(shape, canvas):
    global selected_shape
    selected_shape = shape
    draw_shape(canvas, selected_shape, selected_color)


def select_color(color, canvas):
    global selected_color
    selected_color = color
    draw_shape(canvas, selected_shape, selected_color)

def create_custom_button(canvas, text, command, x, y):
    button_id = canvas.create_text(x, y, text=text, fill="black", activefill="blue", font=("Arial", 10, "underline"))
    canvas.tag_bind(button_id, "<Button-1>", lambda event: command())

def add_labels_and_buttons(canvas):
    canvas.create_text(180, 250, text="Shapes")
    
    create_custom_button(canvas, "Square", lambda: select_shape("square", canvas), 180, 280)
    create_custom_button(canvas, "Circle", lambda: select_shape("circle", canvas), 270, 280)
    create_custom_button(canvas, "Triangle", lambda: select_shape("triangle", canvas), 360, 280)
    
    canvas.create_text(180, 320, text="Colors")
    
    create_custom_button(canvas, "Red", lambda: select_color("red", canvas), 180, 350)
    create_custom_button(canvas, "Green", lambda: select_color("green", canvas), 270, 350)
    create_custom_button(canvas, "Blue", lambda: select_color("blue", canvas), 360, 350)
