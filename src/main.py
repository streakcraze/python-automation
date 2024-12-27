import threading  # Import the threading library for concurrent execution
import time

from scripts.log_rotation import rotate_logs  # Import the rotate_logs function
from scripts.generate_logs import generate_logs  # Import the generate_logs function
from utils.scheduler_helper import schedule_job_every_five_minutes, schedule_job_every_minute  # Import the scheduling functions


def main():
    print("Starting the automation project...")
    
    # event for controlling thread execution
    run_event = threading.Event()
    run_event.set()
    
    # Create threads for each scheduling function
    log_generation_thread = threading.Thread(target=schedule_job_every_minute, args=(generate_logs, run_event))
    log_rotation_thread = threading.Thread(target=schedule_job_every_five_minutes, args=(rotate_logs, run_event))
    
    # Start the scheduling threads
    log_generation_thread.start()
    log_rotation_thread.start()
    
    try:
        # Keep the main thread running to catch KeyboardInterrupt
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        print("Terminating the automation project...")
        run_event.clear()  # Signal the threads to stop
        log_generation_thread.join()
        log_rotation_thread.join()
        print("Automation project successfully terminated.")


if __name__ == "__main__":
    main()