"""This file implements the client-side application that sends coordinates 
 tracking mouse movement and clicked positions to the server."""


import tkinter as tk
import socket
import threading
from utils.utils import draw_shape, add_labels_and_buttons


def update_mouse_position(event):
    try:
        client_socket.send(f"{event.x},{event.y}".encode('utf-8'))
    except ConnectionAbortedError:
        print("Connection was aborted. Unable to send mouse position.")


def send_click_position(event):
    try:
        client_socket.send(f"click,{event.x},{event.y}".encode('utf-8'))
    except ConnectionAbortedError:
        print("Connection was aborted. Unable to send click position.")


def create_tracker_window():
    global canvas, window

    window = tk.Tk()
    window.title("Tracker Window")
    window.geometry("600x400")  # Set the window size to 600x400 pixels

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    # Ensure the canvas captures mouse motion and click events
    canvas.bind('<Motion>', update_mouse_position)
    canvas.bind('<Button-1>', send_click_position)

    add_labels_and_buttons(canvas)
    draw_shape(canvas)  # Draw the default shape

    window.mainloop()


def tracker_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))


if __name__ == "__main__":
    threading.Thread(target=tracker_client).start()
    create_tracker_window()