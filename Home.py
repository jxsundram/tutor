import streamlit as st
from tutor.personal_statement_tutor import PersonalStatementTutor
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the tutor
tutor = PersonalStatementTutor()

# Set up the page
st.set_page_config(
    page_title="Personal Statement Tutor",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Personal Statement Tutor")

# Session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to work on in your personal statement?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = tutor.get_response(prompt)
                st.markdown(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.error("Please ensure your OpenAI API key is correctly set in your .env file")
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
