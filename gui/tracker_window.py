import tkinter as tk
import socket
import threading
from utils import draw_shape, add_labels_and_buttons


def update_mouse_position(event):
    # Calculate the relative position
    canvas_x = canvas.winfo_rootx()
    canvas_y = canvas.winfo_rooty()
    x = event.x_root - canvas_x
    y = event.y_root - canvas_y
    client_socket.send(f"{x},{y}".encode('utf-8'))


def create_window():
    global canvas, window

    window = tk.Tk()
    window.title("Tracker Window")
    window.geometry("600x400")  # Set the window size to 600x400 pixels

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    # Ensure the canvas captures mouse motion events
    canvas.bind('<Motion>', update_mouse_position)

    add_labels_and_buttons(canvas, update_mouse_position)
    draw_shape(canvas)  # Draw the default shape

    window.mainloop()


def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))


if __name__ == "__main__":
    threading.Thread(target=start_client).start()
    create_window()