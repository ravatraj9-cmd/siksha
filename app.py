import streamlit as st
import requests
import json

# --- API Key Setup ---
# Apni API Key yahan quotes ke andar daalein
API_KEY = "YAHAN_APNI_KEY_DAALEIN"

# Is combination ko use karein, ye sabse stable hai
MODEL_NAME = "gemini-1.5-flash"
# Hum v1beta use kar rahe hain kyunki ye saare models support karta hai
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

st.set_page_config(page_title="Siksha AI", page_icon="🎓")
st.title("🤖 Siksha AI (Stable Mode)")

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
        # API Request
        response = requests.post(URL, json=payload)
        result = response.json()

        # Debugging ke liye (Optionally aap is line ko hata sakte hain)
        if "candidates" in result:
            ai_message = result["candidates"][0]["content"]["parts"][0]["text"]
            st.session_state.messages.append({"role": "assistant", "content": ai_message})
            with st.chat_message("assistant"):
                st.write(ai_message)
        else:
            # Agar Error aaye toh details dikhayega
            error_msg = result.get('error', {}).get('message', 'Model Access Issue')
            st.error(f"API Error: {error_msg}")
            st.info("Tip: Agar 'Not Found' aaye toh MODEL_NAME ko 'gemini-pro' karke dekhein.")
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
        
