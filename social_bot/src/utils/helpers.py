from instabot import Bot
from dotenv import load_dotenv
import os

def authenticate_instagram():
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    
    bot = Bot()
    bot.logger.setLevel("CRITICAL")  # Disable instabot logs

    try:
        print("Logging in...")
        bot.login(username=username, password=password)
        print("Login successful.")
    except Exception as e:
        print(f"Error during login: {e}")
    return bot