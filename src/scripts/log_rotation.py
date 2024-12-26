import os  # Import the os library for file and directory operations
import shutil  # Import the shutil library for file operations
from datetime import datetime  # Import the datetime library for timestamping
import gzip  # Import the gzip library for file compression

def rotate_logs():
    log_dir = "/path/to/logs"  # Directory where log files are stored
    archive_dir = "/path/to/archive"  # Directory where archived logs will be stored
    
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
