import streamlit as st
import requests
import json

# --- API Key Setup ---
# Note: Is code ko chalane ke baad apni API Key reset kar lena safety ke liye.
API_KEY = "AIzaSyD-EaJsd1Me8oOjsJrDoG09IjaCcbtDzRw"

# Latest Stable Model (March 2026 update)
# Agar ye bhi na chale toh yahan 'gemini-2.0-flash' likh kar try karein
MODEL_NAME = "gemini-3-flash"
URL = f"https://generativelanguage.googleapis.com/v1/models/{MODEL_NAME}:generateContent?key={API_KEY}"

st.set_page_config(page_title="Siksha AI", page_icon="🎓")
st.title("🤖 Siksha AI (Latest Mode)")

# Chat History Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chats dikhana
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
if prompt := st.chat_input("Puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # API Payload
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        # Request bhejna
        response = requests.post(URL, json=payload)
        result = response.json()

        # Jawab nikalna
        if "candidates" in result:
            ai_message = result["candidates"][0]["content"]["parts"][0]["text"]
            st.session_state.messages.append({"role": "assistant", "content": ai_message})
            with st.chat_message("assistant"):
                st.write(ai_message)
        else:
            # Agar Error aaye toh yahan dikhega
            error_info = result.get('error', {}).get('message', 'Check your API Key or Model Access.')
            st.error(f"API Error: {error_info}")
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
