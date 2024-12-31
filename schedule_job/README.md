# Python Automation Template

This project is a template for automating tasks using Python. It includes scheduling the generation of logs every minute and rotating logs every five minutes. The generated logs are stored in the system's temporary directory, and the rotated logs are compressed and archived within the project's directory to release disk space.
The script uses multithreading to concurrent schedule the generation and rotation of logs at different intervals.

## Project Structure

```
python-automation-template/
│
├── src/
│   ├── main.py
│   ├── scripts/
│   │   ├── generate_logs.py
│   │   ├── log_rotation.py
│   ├── utils/
│   │   ├── scheduler_helper.py
│
├── archive/  # Directory where archived logs are stored
│
├── README.md
│
└── requirements.txt  # List of required packages
```

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/python-automation-template.git
   cd python-automation-template
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

## Running the Project

To start the automation project, run the `main.py` script:
```sh
python src/main.py
```

## Functionality

- **Log Generation**: The project schedules the generation of logs every minute. The logs are stored in the system's temporary directory under the `scheduled_logs` folder.
- **Log Rotation**: The project schedules log rotation every five minutes. During log rotation, the logs in the temporary directory are compressed and archived within the project's `archive` directory to release disk space.

## Practical Considerations

In a practical project, it is recommended to store the archived logs in a database or cloud storage for better management and accessibility.
