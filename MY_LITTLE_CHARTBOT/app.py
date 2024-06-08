import streamlit as st
import joblib
from nltk.chat.util import Chat

# Load chatbot data
Leo, reflections = joblib.load('chatbot_data.pkl')

# Initialize the chatbot
chat = Chat(Leo, reflections)

# Streamlit app
st.title("CollegioBot: Your College Assistant")

# Input text box for user input
user_input = st.text_input("You: ", "Type your message here...")

if st.button("Send"):
    if user_input.lower() == "quit":
        st.write("CollegioBot: Goodbye for now. If you have more questions, feel free to come back!")
    else:
        response = chat.respond(user_input)
        st.write(f"CollegioBot: {response}")

st.write("Note: Type 'quit' to end the conversation.")
