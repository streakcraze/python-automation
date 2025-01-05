import tkinter as tk
import socket
import threading
from PIL import Image, ImageTk
from utils import draw_shape, add_labels_and_buttons


def receive_coordinates():
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
        x, y = map(int, data.split(','))
        # Update the position of the mouse cursor
        canvas.coords(mouse_cursor, x, y)

    client_socket.close()


def create_window():
    global canvas, mouse_cursor, cursor_image

    window = tk.Tk()
    window.title("Receiver Window")
    window.geometry("600x400")  # Set the window size to 600x400 pixels

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    add_labels_and_buttons(canvas)
    draw_shape(canvas)  # Draw the default shape

    # Load and resize the mouse cursor image using Pillow
    image = Image.open("cursor.png")
    image = image.resize((20, 20), Image.LANCZOS)  # Resize the image to 20x20 pixels
    cursor_image = ImageTk.PhotoImage(image)
    mouse_cursor = canvas.create_image(0, 0, anchor="nw", image=cursor_image)
    canvas.tag_raise(mouse_cursor) # Ensure the mouse cursor is above other elements

    window.mainloop()


if __name__ == "__main__":
    threading.Thread(target=receive_coordinates).start()
    create_window()