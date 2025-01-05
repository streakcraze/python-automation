"""This file implements the server-side application that receives mouse coordinates
 and updates the position of a cursor on the canvas."""


import tkinter as tk
import socket
import threading
from PIL import Image, ImageTk
from utils.utils import draw_shape, add_labels_and_buttons
import autoit


def handle_click_event(x, y):
    # Adjust coordinates to account for the receiver window's position on the screen
    x += window.winfo_rootx()
    y += window.winfo_rooty()
    # Temporarily hide the mouse cursor image
    canvas.itemconfigure(mouse_cursor, state='hidden')
    # Use autoit to initiate a mouse click at the adjusted coordinates
    autoit.mouse_click("left", x, y)
    # Show the mouse cursor image again
    canvas.itemconfigure(mouse_cursor, state='normal')


def update_cursor_position(x, y):
    # Update the position of the mouse cursor
    canvas.coords(mouse_cursor, x, y)
    # Ensure the mouse cursor is above other elements
    canvas.tag_raise(mouse_cursor)


def load_cursor_image():
    global mouse_cursor
    # Load and resize the mouse cursor image using Pillow
    image = Image.open("static/cursor.png")
    image = image.resize((15, 15), Image.LANCZOS)  # Resize the image to 20x20 pixels
    cursor_image = ImageTk.PhotoImage(image)
    mouse_cursor = canvas.create_image(0, 0, anchor="nw", image=cursor_image)


def receiver_client():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(1)
    print("Receiver listening on port 9999")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        parts = data.split(',')
        if len(parts) == 3 and parts[0] == "click":
            _, x, y = parts
            x, y = int(x), int(y)
            handle_click_event(x, y)
        elif len(parts) == 2:
            x, y = map(int, parts)
            update_cursor_position(x, y)

    client_socket.close()


def create_receiver_window():
    global canvas, window

    window = tk.Tk()
    window.title("Receiver Window")
    window.geometry("600x400")  # Set the window size to 600x400 pixels

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    add_labels_and_buttons(canvas)
    # Draw the default shape
    draw_shape(canvas)
    load_cursor_image()

    window.mainloop()


if __name__ == "__main__":
    threading.Thread(target=receiver_client).start()
    create_receiver_window()