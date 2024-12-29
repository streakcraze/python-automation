import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_chatbot():
    # Initialize the Google Generative AI configuration
    api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)
    gemini_model = genai.GenerativeModel("gemini-pro")
    chat = gemini_model.start_chat(history=[])
    return chat
