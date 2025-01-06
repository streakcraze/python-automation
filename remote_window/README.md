# Python GUI Automation Project

This project demonstrates mouse tracking and interaction replication across two windows using a client-server setup. It beautifully interweaves `tkinter`, `sockets`, `threading`, and `pyautoit` to achieve these functionalities.

## Project Structure

```
python-automation/
│
├── README.md                # Project overview and instructions
├── requirements.txt         # List of dependencies
├── tracker_window.py        # Client-side application that sends mouse coordinates
├── receiver_window.py       # Server-side application that receives mouse coordinates
├── utils/
│   └── helpers.py           # Utility functions for mouse interactions
└── static/                  # Stores static files, e.g., images
    └── cursor.png           
```

## Features

1. **Mouse Tracking**:
   - The `tracker_window.py` sends the mouse coordinates to the server.
   - The `receiver_window.py` receives the coordinates and updates the position of a cursor image on the canvas.

2. **Mouse Interaction Replication**:
   - Click events in the tracker window are replicated in the receiver window using `pyautoit`. Both windows have selectable shapes and colors to show these interactions.

## How to Run

1. **Clone the repository**:
   ```sh
   git clone https://github.com/streakcraze/python-automation.git
   cd remote_window
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Start the Server**:
   - Run `receiver_window.py` to start the server that listens for incoming mouse coordinates.

   ```sh
   python receiver_window.py
   ```

5. **Start the Client**:
   - Run `tracker_window.py` to start the client that sends mouse coordinates to the server.

   ```sh
   python tracker_window.py
   ```

## Dependencies

- `Pillow`: Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.
- `pyautoit`: Python wrapper for AutoIt.

## License

This project is licensed under the MIT License.