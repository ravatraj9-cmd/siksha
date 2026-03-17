import streamlit as st
import google.generativeai as genai

# 1. API Key Setup
# Is key ko safe rakhne ke liye st.secrets use karna recommend hai
genai.configure(api_key="AIzaSyDUO1nj1qknykSksY82SVCAW0DkowNNY1c")

# 2. Model Initialisation 
# Yahan 'models/' hatakar try kijiye ya 'gemini-1.5-flash-latest' likhiye
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    model = genai.GenerativeModel('gemini-pro') # Fallback agar flash na mile

st.title("🤖 Siksha AI")

# 3. Chat History Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chats dikhana
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 4. User Input aur Response
if prompt := st.chat_input("Puchiye apna sawaal..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Generate content
        response = model.generate_content(prompt)
        
        if response.text:
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.chat_message("assistant").write(response.text)
        else:
            st.error("Model ne koi response nahi diya. Safety filters check karein.")
            
    except Exception as e:
        st.error(f"Error: {e}")
