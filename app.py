import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# 1. API Setup
genai.configure(api_key="AIzaSyDUO1nj1qknykSksY82SVCAW0DkowNNY1c")

# 2. Model Setup (Version fix kiya hai taaki v1beta ka error na aaye)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Siksha AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # MAGIC LINE: Yahan hum version 'v1' force kar rahe hain
        response = model.generate_content(
            prompt, 
            request_options=RequestOptions(api_version='v1')
        )
        
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.chat_message("assistant").write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
