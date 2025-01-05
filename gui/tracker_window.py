import tkinter as tk
import socket
import threading
from utils import draw_shape, add_labels_and_buttons

selected_shape = "square"
selected_color = "red"

def update_mouse_position(event):
    send_coordinates(event.x, event.y)

def send_coordinates(x, y):
    client_socket.send(f"{x},{y}".encode('utf-8'))

def create_window():
    global canvas
    window = tk.Tk()
    window.title("Tracker Window")
    window.geometry("600x400")  # Set the window size to 600x400 pixels

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    add_labels_and_buttons(canvas)
    draw_shape(canvas, selected_shape, selected_color)  # Draw the default shape

    window.bind('<Motion>', update_mouse_position)

    window.mainloop()

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))

if __name__ == "__main__":
    threading.Thread(target=start_client).start()
    create_window()