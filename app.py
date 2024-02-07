# Import necessary libraries
import streamlit as st
from gtts import gTTS
from io import BytesIO

# Set Streamlit title
st.title("Text-to-Speech App")

# Add a textarea for user input
user_input = st.text_area("Enter the text you want to convert to speech:")

# Function to convert text to speech
def text_to_speech(text):
    # Create a Text-to-Speech object
    tts = gTTS(text=text, lang='en')
    
    # Save the speech as a BytesIO object
    speech_bytes = BytesIO()
    tts.write_to_fp(speech_bytes)
    
    return speech_bytes

# Check if the user has entered any text
if user_input:
    # Add a button to trigger text-to-speech conversion
    if st.button("Convert to Speech"):
        # Convert text to speech
        speech_bytes = text_to_speech(user_input)
        
        # Display the audio player for the generated speech
        st.audio(speech_bytes, format='audio/wav')
