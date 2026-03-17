import streamlit as st
import requests
import json

# API Key
API_KEY = "AIzaSyDUO1nj1qknykSksY82SVCAW0DkowNNY1c"
# Google API URL (Seedha rasta)
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.title("🤖 Siksha AI (Stable Mode)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # API Payload (Data jo hum bhej rahe hain)
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        # Seedha Google ko request bhejna
        response = requests.post(URL, json=payload)
        result = response.json()

        # Jawab nikalna
        if "candidates" in result:
            ai_message = result["candidates"][0]["content"]["parts"][0]["text"]
            st.session_state.messages.append({"role": "assistant", "content": ai_message})
            st.chat_message("assistant").write(ai_message)
        else:
            # Agar API Key mein dikat hogi toh yahan pakdi jayegi
            st.error(f"API Error: {result.get('error', {}).get('message', 'Unknown Error')}")
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
