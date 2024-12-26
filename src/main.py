from scripts.log_rotation import rotate_logs  # Import the rotate_logs function
from utils.scheduler_helper import schedule_job_every_five_minutes  # Import the schedule_job_every_five_minutes function

def main():
    print("Starting the automation project...")
    schedule_job_every_five_minutes(rotate_logs)  # Schedule the log rotation task

if __name__ == "__main__":
    main()