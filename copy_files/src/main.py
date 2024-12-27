def main():
    print("Starting the automation project...")
    
    # Importing the example script and utility functions
    from scripts.example_script import copy_files
    from utils.helpers import log_message

    # Log the start of the example script
    log_message("Running example script...")
    
    # Execute the example script
    copy_files()

if __name__ == "__main__":
    main()