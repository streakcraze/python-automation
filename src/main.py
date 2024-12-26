from scripts.log_rotation import rotate_logs  # Import the rotate_logs function
from scripts.generate_logs import generate_logs  # Import the generate_logs function
from utils.scheduler_helper import schedule_job_every_five_minutes, schedule_job_every_minute  # Import the scheduling functions

def main():
    print("Starting the automation project...")
    schedule_job_every_minute(generate_logs)  # Schedule the log generation task every minute
    schedule_job_every_five_minutes(rotate_logs)  # Schedule the log rotation task

if __name__ == "__main__":
    main()