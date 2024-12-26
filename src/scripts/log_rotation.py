import os  # Import the os library for file and directory operations
import shutil  # Import the shutil library for file operations
from datetime import datetime  # Import the datetime library for timestamping
import gzip  # Import the gzip library for file compression
import tempfile  # Import the tempfile library for creating temporary directories

def rotate_logs():
    print("Rotating logs...")  # Print a message indicating that logs are being rotated
    
    temp_dir = tempfile.gettempdir()  # Get the system's temporary directory
    log_dir = os.path.join(temp_dir, "scheduled_logs")  # Directory where log files are stored
    archive_dir = os.path.join(os.path.dirname(__file__), "../../archive")  # Directory where archived logs will be stored
    
    if not os.path.exists(log_dir):  # Check if log directory exists
        print("No logs found.")  # Print a message indicating that no logs were found
        return  # Terminate the function
    
    if not os.path.exists(archive_dir):  # Check if archive directory exists
        os.makedirs(archive_dir)  # Create archive directory if it doesn't exist
    
    for log_file in os.listdir(log_dir):  # Iterate over all files in the log directory
        if log_file.endswith(".log"):  # Check if the file is a log file
            log_path = os.path.join(log_dir, log_file)  # Full path to the log file
            archive_path = os.path.join(archive_dir, f"{log_file}-{datetime.now().strftime('%Y%m%d%H%M%S')}.gz")  # Full path to the archived log file with timestamp
            with open(log_path, 'rb') as f_in, gzip.open(archive_path, 'wb') as f_out:  # Open the log file and the archive file
                shutil.copyfileobj(f_in, f_out)  # Copy the log file to the archive file
            os.remove(log_path)  # Remove the original log file
    
    print("Logs rotated.")  # Print a message indicating that logs have been rotated
