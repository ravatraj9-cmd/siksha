import streamlit as st
import google.generativeai as genai

# 1. API Configuration
# Maine check kiya hai, ye key sahi format mein hai
genai.configure(api_key="AIzaSyDUO1nj1qknykSksY82SVCAW0DkowNNY1c")

# 2. Model Setup
# 'gemini-pro' use kar rahe hain kyunki ye 0.5.4 library ke saath best chalta hai
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Siksha AI", page_icon="🤖")
st.title("🤖 Siksha AI")
st.caption("Powered by Google Gemini")

# 3. Chat History Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Purani messages dikhana
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 5. User Input
if prompt := st.chat_input("Puchiye apna sawal..."):
    # User ka message save aur display karo
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # AI se response mangwana
        with st.spinner("Soch raha hoon..."):
            response = model.generate_content(prompt)
            
            # Response ko screen par dikhana
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.chat_message("assistant").write(response.text)
            
    except Exception as e:
        # Agar koi error aaye toh yahan dikhega
        st.error(f"Error aa gaya bhai: {e}")
        
