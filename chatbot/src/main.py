from utils.chatbot_helper import initialize_chatbot
from scripts.chatbot_script import run_chatbot
import streamlit as st

def main():
    chatbot = initialize_chatbot()
    run_chatbot(chatbot)

if __name__ == "__main__":
    st.set_page_config(page_title="Chatbot")
    main()
