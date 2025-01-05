import tkinter as tk

selected_shape = "square"
selected_color = "red"

def draw_shape(canvas, selected_shape, selected_color):
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

def add_labels_and_buttons(canvas):
    tk.Label(canvas, text="Shapes").place(x=180, y=250)
    tk.Button(canvas, text="Square", command=lambda: select_shape("square", canvas)).place(x=180, y=280)
    tk.Button(canvas, text="Circle", command=lambda: select_shape("circle", canvas)).place(x=270, y=280)
    tk.Button(canvas, text="Triangle", command=lambda: select_shape("triangle", canvas)).place(x=360, y=280)

    tk.Label(canvas, text="Colors").place(x=180, y=320)
    tk.Button(canvas, text="Red", command=lambda: select_color("red", canvas)).place(x=180, y=350)
    tk.Button(canvas, text="Green", command=lambda: select_color("green", canvas)).place(x=270, y=350)
    tk.Button(canvas, text="Blue", command=lambda: select_color("blue", canvas)).place(x=360, y=350)
