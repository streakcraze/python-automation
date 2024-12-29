import streamlit as st

def run_chatbot(chatbot):
    st.title("Chatbot")
    st.write("Welcome to the chatbot. Type 'exit' to end the conversation.")
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    
    user_input = st.text_input("You: ", key="user_input")
    submit_button = st.button("Send")

    if submit_button and user_input:
        if user_input.lower() == 'exit':
            st.write("Chatbot: Goodbye!")
        else:
            response = chatbot.send_message(user_input, stream=True)
            st.session_state.conversation.append(f"You: {user_input}")
            full_response = ""
            for output_chunk in response:
                full_response += output_chunk.text
            st.session_state.conversation.append(f"Chatbot: {full_response}")
    
    for message in st.session_state.conversation:
        st.write(message)