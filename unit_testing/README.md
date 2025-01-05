# Automated Testing Project

This project showcases the automation of Python testing using the `unittest` framework, Flask routes with basic authentication, and SQLite database integration.

## Project Structure

```
automated-testing/
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── src/
│   ├── __init__.py
│   ├── main.py
├── requirements.txt
├── README.md
├── .gitignore
```

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/streakcraze/python-automation.git
   cd unit_testing
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

## Usage

Execute the following command to run the tests:
```sh
python -m unittest discover -s tests
```
