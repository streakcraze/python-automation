# Python GUI Automation Project

This project consists of a simple GUI application that allows users to draw shapes and select colors on a canvas. Additionally, it includes a client-server setup to track and display mouse movements across two windows.

## Project Structure

- `utils.py`: Contains utility functions for drawing shapes, selecting shapes and colors, and adding labels and buttons to the canvas.
- `tracker_window.py`: Implements the client-side application that sends mouse coordinates to the server.
- `receiver_window.py`: Implements the server-side application that receives mouse coordinates and updates the position of a cursor on the canvas.

## Features

1. **Shape Drawing**:
   - Users can select from three shapes: square, circle, and triangle.
   - Users can select from three colors: red, green, and blue.
   - The selected shape and color are drawn on the canvas at a fixed position.

2. **Mouse Tracking**:
   - The `tracker_window.py` sends the mouse coordinates to the server.
   - The `receiver_window.py` receives the coordinates and updates the position of a cursor image on the canvas.

## How to Run

1. **Start the Server**:
   - Run `receiver_window.py` to start the server that listens for incoming mouse coordinates.

   ```sh
   python receiver_window.py
   ```

2. **Start the Client**:
   - Run `tracker_window.py` to start the client that sends mouse coordinates to the server.

   ```sh
   python tracker_window.py
   ```

## Dependencies

- `tkinter`: Standard Python interface to the Tk GUI toolkit.
- `Pillow`: Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.

Install Pillow using pip:

```sh
pip install pillow
```

## Notes

- Ensure that the `cursor.png` image file is present in the same directory as `receiver_window.py`.
- The server listens on port `9999` and the client connects to `127.0.0.1` on port `9999`.

## License

This project is licensed under the MIT License.