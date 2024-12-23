def main():
    print("Starting the automation project...")
    
    # Importing the example script and utility functions
    from scripts.example_script import run_example
    from utils.helpers import log_message

    # Log the start of the example script
    log_message("Running example script...")
    
    # Execute the example script
    run_example()

if __name__ == "__main__":
    main()