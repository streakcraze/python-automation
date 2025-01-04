import tkinter as tk
import socket
import threading

def update_mouse_position(event):
    send_coordinates(event.x, event.y)

def send_coordinates(x, y):
    client_socket.send(f"{x},{y}".encode('utf-8'))

def create_window():
    window = tk.Tk()
    window.title("Tracker Window")
    window.geometry("400x300")  # Set the window size to 400x300 pixels

    window.bind('<Motion>', update_mouse_position)

    window.mainloop()

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))

if __name__ == "__main__":
    threading.Thread(target=start_client).start()
    create_window()