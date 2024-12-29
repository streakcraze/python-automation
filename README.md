# Python Automation Projects Collection

This repository is a collection of different Python automation projects. Each project is designed to automate specific tasks using Python scripts and utilities.

## Projects

### 1. Template
This project serves as a template for automating tasks using Python. It includes example scripts and utility functions that can be customized for various automation tasks.

**Project Structure:**
```
template/
├── src/
│   ├── main.py          # Entry point of the automation project
│   ├── utils/
│   │   └── helpers.py   # Utility functions for scripts
│   └── scripts/
│       └── example_script.py  # Example automation script
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

### 2. Copy Files
This project automates the process of copying files from a source directory to a destination directory as defined in `directories.txt`.

**Project Structure:**
```
copy_files/
├── src/
│   ├── main.py          # Entry point of the automation project
│   ├── utils/
│   │   └── helpers.py   # Utility functions for scripts
│   └── scripts/
│       └── example_script.py  # Example automation script
├── requirements.txt     # Project dependencies
├── directories.txt      # Source and destination directories
└── README.md            # Project documentation
```

### 3. Schedule Job
This project schedules the generation of logs every minute and rotates logs every five minutes. The generated logs are stored in the system's temporary directory, and the rotated logs are compressed and archived within the project's directory to release disk space.

**Project Structure:**
```
schedule_job/
├── src/
│   ├── main.py
│   ├── scripts/
│   │   ├── generate_logs.py
│   │   ├── log_rotation.py
│   ├── utils/
│   │   └── scheduler_helper.py
├── archive/  # Directory where archived logs are stored
├── requirements.txt  # List of required packages
└── README.md
```

### 4. Chatbot
This project implements a simple chatbot using Python. The chatbot can respond to predefined questions and can be extended with more functionalities.

**Project Structure:**
```
chatbot/
├── src/
│   ├── main.py          # Entry point of the chatbot project
│   ├── utils/
│   │   └── chatbot_helper.py   # Utility function creating the chatbot
│   └── scripts/
│       └── chatbot_script.py  # Script for training the chatbot
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

For each project, follow these steps to set up and run the automation scripts:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/python-automation-projects.git
   cd python-automation-projects/<project-directory>
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

4. **Run the main script**:
   ```sh
   python src/main.py
   ```

For more specific usage of individual scripts, refer to their respective documentation within the script files.