# Simple Chatbot

This project is designed to implement a simple chatbot using the `streamlit` and `google-generativeai` libraries.

## Project Structure

```
chatbot/
├── src/
│   ├── main.py          # Entry point of the chatbot project
│   ├── utils/
│   │   └── chatbot_helper.py   # Utility functions for the chatbot
│   └── scripts/
│       └── chatbot_script.py   # Script functions for the chatbot
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/python-automation.git
   cd chatbot
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

4. **Set up the API key**:
   - Obtain your API key from [Google AI Studio](https://aistudio.google.com/apikey).
   - Create a `.env` file in the root of the project and add your API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

To run the chatbot, execute the main script:
```
streamlit run src/main.py
```

The script will initialize the chatbot and allow you to interact with it. Type `exit` to end the conversation.

## Requirements

- `streamlit`
- `google-generativeai`
- `python-dotenv`
