import threading  # Import the threading library for concurrent execution

from scripts.log_rotation import rotate_logs  # Import the rotate_logs function
from scripts.generate_logs import generate_logs  # Import the generate_logs function
from utils.scheduler_helper import schedule_job_every_five_minutes, schedule_job_every_minute  # Import the scheduling functions

def main():
    print("Starting the automation project...")
    
    # Create a stop flag for thread termination
    stop_flag = threading.Event()
    
    # Create threads for each scheduling function
    log_generation_thread = threading.Thread(target=schedule_job_every_minute, args=(generate_logs, stop_flag))
    log_rotation_thread = threading.Thread(target=schedule_job_every_five_minutes, args=(rotate_logs, stop_flag))
    
    # Start the scheduling threads
    log_generation_thread.start()
    log_rotation_thread.start()
    
    try:
        # Keep the main thread running to catch KeyboardInterrupt
        while log_generation_thread.is_alive() and log_rotation_thread.is_alive():
            log_generation_thread.join(timeout=1)
            log_rotation_thread.join(timeout=1)
    except KeyboardInterrupt:
        print("Terminating the automation project...")
        stop_flag.set()  # Signal the threads to stop
        log_generation_thread.join()
        log_rotation_thread.join()

if __name__ == "__main__":
    main()