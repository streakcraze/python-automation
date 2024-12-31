# Social Bot Automation

This project automates the process of gathering Instagram analytics of a specified user using `instabot`.

## Project Structure

```
template/
├── src/
│   ├── main.py          # Entry point of the automation project
│   ├── utils/
│   │   └── helpers.py   # Utility functions for scripts
│   └── scripts/
│       └── instagram_analytics.py  # Script to gather Instagram analytics
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd social_bot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Instagram credentials:
    ```plaintext
    INSTAGRAM_USERNAME=your_username
    INSTAGRAM_PASSWORD=your_password
    ```

4. Specify the user to be analyzed in `specified_user.txt`:
    ```plaintext
    username=cristiano
    ```

## Usage

Run the main script to gather Instagram analytics:
```sh
python src/main.py
```

## Functionality

- **Top Posts**: Retrieve the top posts from a specified user.
- **Comment Analysis**: Gather comments from each post and analyze sentiments.

## License

This project is licensed under the MIT License.