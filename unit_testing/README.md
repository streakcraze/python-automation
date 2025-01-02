# Automated Testing Project

This project showcases the automation of Python testing using the `unittest` framework and Flask routes.

## Project Structure

```
automated-testing/
├── tests/
│   ├── __init__.py
│   ├── test_sample.py
├── src/
│   ├── __init__.py
│   ├── sample.py
├── requirements.txt
├── README.md
├── .gitignore
```

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Flask App

To run the Flask app, execute the following command:
```sh
python src/sample.py
```

## Running Tests

To run the tests, execute the following command:
```sh
python -m unittest discover -s tests
```
