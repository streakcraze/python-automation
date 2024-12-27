import os  # Import the os library for file and directory operations
import tempfile  # Import the tempfile library for creating temporary directories
from datetime import datetime  # Import the datetime library for timestamping

def generate_logs():
    temp_dir = tempfile.gettempdir()  # Get the system's temporary directory
    log_dir = os.path.join(temp_dir, "scheduled_logs")  # Create a logs directory within the temporary directory
    
    if not os.path.exists(log_dir):  # Check if the log directory exists
        os.makedirs(log_dir)  # Create the log directory if it doesn't exist
    
    log_file = os.path.join(log_dir, f"log-{datetime.now().strftime('%Y%m%d%H%M%S')}.log")  # Create a log file with a timestamp
    with open(log_file, 'w') as f:  # Open the log file for writing
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current timestamp
        f.write(f"[{timestamp}] This is a log entry.\n")  # Write a log entry with the timestamp to the file
    
    print(f"Log generated: {log_file}")  # Print a message indicating that the log has been generated
