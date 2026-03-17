import streamlit as st
import requests
import json

# --- API Key Setup ---
# Nayi key banakar yahan zaroor daalna, purani shayad block ho gayi ho
API_KEY = "AIzaSyD-EaJsd1Me8oOjsJrDoG09IjaCcbtDzRw"

# 1. Sabse pehle ise try karein: "gemini-1.5-flash"
# 2. Agar na chale toh ise try karein: "gemini-pro"
MODEL_NAME = "gemini-1.5-flash"

# VERSION: Yahan 'v1beta' hi rehne dein, ye sabse stable hai requests ke liye
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

st.set_page_config(page_title="Siksha AI", page_icon="🎓")
st.title("🤖 Siksha AI (Stable Fix)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(URL, json=payload)
        result = response.json()

        if "candidates" in result:
            ai_message = result["candidates"][0]["content"]["parts"][0]["text"]
            st.session_state.messages.append({"role": "assistant", "content": ai_message})
            with st.chat_message("assistant"):
                st.write(ai_message)
        else:
            # Error check karne ke liye
            error_msg = result.get('error', {}).get('message', 'Unknown Error')
            st.error(f"API Error: {error_msg}")
            st.info(f"Model tried: {MODEL_NAME} on v1beta")
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
        
