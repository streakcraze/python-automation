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
    
    # Gather User Analytics
    username = "arnold_odhis"
    gather_instagram_analytics(bot, username)
    

if __name__ == "__main__":
    main()
