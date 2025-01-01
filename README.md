# Python Automation Projects Collection

This repository is a collection of different Python automation projects. Each project is designed to automate specific tasks using Python scripts and utilities.

## Projects

### 1. Template
This project serves as a template for automating tasks using Python. It includes example scripts and utility functions that can be customized for various automation tasks.

### 2. Copy Files
This project automates the process of copying files from a source directory to a destination directory as defined in `directories.txt`.

### 3. Schedule Job
This project schedules the generation of logs every minute and rotates logs every five minutes. The generated logs are stored in the system's temporary directory, and the rotated logs are compressed and archived within the project's directory to release disk space. The script uses multithreading to concurrently schedule the generation and rotation of logs at different intervals.

### 4. Chatbot
This project implements a simple chatbot using Python. The chatbot can respond to predefined questions and can be extended with more functionalities. It utilizes the `google-generativeai` SDK and the `Gemini` model for generating responses.

### 5. Social Bot
This project automates the process of gathering Instagram analytics of a specified user using `instabot`. The analytics include the top posts and the average sentiments of their comments.

### 6. Testing
This project showcases the automation of Python testing using the `unittest` framework. It includes sample functions and their corresponding test cases.

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
