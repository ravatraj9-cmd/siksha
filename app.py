import streamlit as st
from google import genai

# Sahi API Key yahan dalo
client = genai.Client(api_key="AIzaSyDUO1nj1qknykSksY82SVCAW0DkowNNY1c")

st.title("🤖 Siksha AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Nayi library ka syntax
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.chat_message("assistant").write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
        
