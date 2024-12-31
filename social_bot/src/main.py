from utils.helpers import authenticate_instagram
from scripts.instagram_analytics import gather_instagram_analytics
import shutil
import os

def main():
    # Delete the config folder
    config_folder = os.path.join(os.path.dirname(__file__), '..', 'config')
    if os.path.exists(config_folder):
        shutil.rmtree(config_folder)
        print("Config folder deleted.")

    # Authenticate Admin
    bot = authenticate_instagram()
    if bot is None:
        print("Failed to authenticate Instagram. Exiting...")
        return
    
    # Extract username from specified_user.txt
    user_file = os.path.join(os.path.dirname(__file__), '..', 'specified_user.txt')
    if not os.path.exists(user_file):
        print("specified_user.txt not found. Exiting...")
        return
    
    with open(user_file, 'r') as file:
        line = file.readline().strip()
        if line.startswith("username="):
            username = line.split("=", 1)[1].strip()
        else:
            print("Invalid format in specified_user.txt. Exiting...")
            return
    
    if not username:
        print("No username specified in specified_user.txt. Exiting...")
        return
    
    # Gather User Analytics
    gather_instagram_analytics(bot, username)

if __name__ == "__main__":
    main()
