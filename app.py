import streamlit as st
import google.generativeai as genai

# Apni API Key yahan dalo
genai.configure(api_key="TERI_API_KEY_YAHAN_DALO")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Siksha AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.chat_message("assistant").write(response.text)
  
