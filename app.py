import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI API key
genai.configure(api_key='AIzaSyCABGD7ZfFR4_OCJW2CpLvx_97E8fCv_24')

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize session state to hold conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to handle chat with the Generative AI model
def chat_with_model(user_input):
    # Append user input to the conversation history
    st.session_state.history.append({"role": "user", "parts": user_input})
    
    # Start a new chat session with the history and get the model's response
    chat = model.start_chat(history=st.session_state.history)
    response = chat.send_message(user_input)
    
    # Append model response to the history
    st.session_state.history.append({"role": "model", "parts": response.text})
    
    return response.text

# Streamlit UI
st.title("Chat with Google Generative AI")

# Get user input
user_input = st.text_input("Enter your message:", "")

# Check if user has entered a message
if user_input:
    # Get model response
    response_text = chat_with_model(user_input)
    st.text_area("Response", response_text, height=200)
    
    # Clear input box after sending message
    st.text_input("Enter your message:", "", key="user_input_clear")

# Display conversation history
for message in st.session_state.history:
    if message["role"] == "user":
        st.write(f"**You:** {message['parts']}")
    elif message["role"] == "model":
        st.write(f"**Model:** {message['parts']}")
